import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Boxplot with Mean Values")

    # ファイルのアップロード
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # アップロードされたCSVファイルをDataFrameに読み込む
        data = pd.read_csv(uploaded_file)
        
        st.write("### Uploaded Data:")
        st.write(data)
        
        # 1列目の文字列でグループ分けして、グループ名をカラム名に設定して結合
        grouped_dataframes = []
        for group_name, group_data in data.groupby(data.columns[0]):
            group_df = pd.DataFrame({group_name: group_data[data.columns[1]].values})
            grouped_dataframes.append(group_df)

        # グループごとのデータフレームを縦方向に連結して新しいデータフレームを作成
        merged_df = pd.concat(grouped_dataframes, axis=1)

        # 外れ値を除去する関数
        def remove_outliers(df, col):
            numeric_df = df[pd.to_numeric(df[col], errors='coerce').notnull()]
            Q1 = numeric_df[col].quantile(0.25)
            Q3 = numeric_df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            return numeric_df[(numeric_df[col] >= lower_bound) & (numeric_df[col] <= upper_bound)]

        # 列ごとに外れ値を除去したデータフレームを作成
        df_no_outliers = pd.DataFrame()
        for col in merged_df.columns:
            df_no_outliers[col] = remove_outliers(merged_df, col)[col]

        # 箱ひげ図を描画
        plt.figure(figsize=(8, 6))
        sns.boxplot(data=df_no_outliers, orient='v', color='white', fliersize=5, showmeans=True, meanprops={"marker":"x", "markerfacecolor":"black", "markeredgecolor":"black", "markersize":10})

        plt.xlabel("Variables")
        plt.ylabel("Values")
        plt.title("Boxplot with Mean Values")

        st.pyplot(plt)

if __name__ == "__main__":
    main()
