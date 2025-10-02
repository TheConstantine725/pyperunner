import marimo

__generated_with = "0.16.4"
app = marimo.App(width="full")


@app.cell
def _():
    return


@app.cell
def _():
    import duckdb
    main_duck = duckdb.connect("~/databases/main_duck.ddb")
    starter = duckdb.connect("~/projects/python/pyperunner/.databases/main.ddb")
    return (starter,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo, starter):
    _df = mo.sql(
        f"""
        SELECT * FROM landing.data;
        """,
        engine=starter
    )
    return


if __name__ == "__main__":
    app.run()
