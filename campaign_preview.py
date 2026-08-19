from config.sample_campaign import campaign
from database.repository import Repository
from services.sql_builder import SQLBuilder
from services.preview_engine import PreviewEngine


def main():

    repository = Repository()
    sql_builder = SQLBuilder()

    engine = PreviewEngine(
        repository,
        sql_builder
    )

    engine.run(campaign)


if __name__ == "__main__":
    main()