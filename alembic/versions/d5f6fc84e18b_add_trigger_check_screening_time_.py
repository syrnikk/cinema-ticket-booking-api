"""Add TRIGGER check_screening_time_overlap_trigger 

Revision ID: d5f6fc84e18b
Revises: 35a4f99106a4
Create Date: 2023-05-20 00:33:35.760548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5f6fc84e18b'
down_revision = '35a4f99106a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
            CREATE OR REPLACE FUNCTION check_screening_time_overlap()
            RETURNS TRIGGER AS $$
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM screenings s
                    JOIN repertoire r ON s.repertoire_id = r.id
                    JOIN movies m ON r.movie_id = m.id
                    WHERE r.cinema_id = (SELECT cinema_id FROM repertoire r2 WHERE r2.id = NEW.repertoire_id)
                        AND s.room_number = NEW.room_number
                        AND (NEW.start_time BETWEEN s.start_time AND (s.start_time + (m.duration_minutes || ' minutes')::INTERVAL)
                            OR (NEW.start_time + ((SELECT m2.duration_minutes FROM repertoire r2 JOIN movies m2 ON r2.movie_id = m2.id WHERE r2.id = NEW.repertoire_id) || ' minutes')::INTERVAL) BETWEEN s.start_time AND (s.start_time + (m.duration_minutes || ' minutes')::INTERVAL))
                ) THEN
                    RAISE EXCEPTION 'Screening time overlaps with another screening.';
                END IF;
            
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
            
            
            
            CREATE TRIGGER check_screening_time_overlap_trigger
            BEFORE INSERT ON screenings
            FOR EACH ROW
            EXECUTE FUNCTION check_screening_time_overlap();
        """)


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS check_screening_time_overlap_trigger ON screenings")
    op.execute("DROP FUNCTION IF EXISTS check_screening_time_overlap()")
