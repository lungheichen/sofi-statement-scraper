import tabula as tb
import pandas as pd
import re
import os


if __name__ == "__main__":
    # list files
    files = os.listdir("statements")

    df_all = pd.DataFrame(columns=["DATE", "TYPE", "DESCRIPTION", "AMOUNT", "BALANCE"])

    transformed_dfs = [df_all]  # Stores all dfs after removing NaNs, etc

    for file in files:
        pdf = os.path.join("statements", file)

        # current_page_transformed_dfs = []

        # Read pdf into a list of DataFrame
        page_one_dfs = tb.read_pdf(
            os.path.join("statements", file),
            pages="1",
            multiple_tables=False,
            area=(400, 0, 550, 600),
            lattice=True,
            pandas_options={
                "names": ["DATE", "TYPE", "DESCRIPTION", "AMOUNT", "BALANCE"],
                "header": None,
            },
        )

        df2 = page_one_dfs[0]
        df2.iloc[:, 0] = pd.to_datetime(
            df2.iloc[:, 0], format="%b %d, %Y", errors="coerce"
        )

        if df2.empty:
            continue
        transformed_dfs.append(df2)

        # next_page_dfs =
        page_two_dfs = tb.read_pdf(
            os.path.join("statements", file),
            pages="2",
            lattice=True,
            multiple_tables=False,
            area=(40, 0, 800, 600),
            columns=[100, 200, 400, 500, 600],
            pandas_options={
                "header": None,
            },
        )

        df1 = page_two_dfs[0]

        df1.iloc[:, 0] = pd.to_datetime(
            df1.iloc[:, 0], format="%b %d, %Y", errors="coerce"
        )

        bad_indices = df1[df1[0].isnull()]
        if len(bad_indices) > 0:
            first_bad_index = bad_indices.index[0]
        else:
            first_bad_index = -1
        df1 = df1[:first_bad_index].dropna(axis=1)

        # if len(df1.columns) > 0:
        if not df1.empty:
            df1.columns = ["DATE", "TYPE", "DESCRIPTION", "AMOUNT", "BALANCE"]
            transformed_dfs.append(df1)

        # # Read remote pdf into a list of DataFrame
        # page_two_dfs = tb.read_pdf(
        #     "https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf"
        # )

        # # convert PDF into CSV
        # tb.convert_into(pdf, "output.csv", output_format="csv", pages="1")

        # # convert all PDFs in a directory
        # tb.convert_into_by_batch("input_directory", output_format="csv", pages="all")

    # for df in modified_dfs:
    #     df_all = pd.concat([df_all, df], ignore_index=True)
    df_all = pd.concat(transformed_dfs, ignore_index=True)
    df_all.to_csv("SoFi_statements.csv", index=False)
