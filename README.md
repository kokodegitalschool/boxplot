# 箱ひげ図の作成プロジェクト

このプロジェクトでは、Pythonを使用して箱ひげ図を作成する方法を提供しています。箱ひげ図は、データの分布や外れ値を視覚化するのに役立つグラフです。このREADMEでは、プロジェクトの概要、インストール方法、使い方について説明します。

## 概要

このプロジェクトは、Pythonとデータ処理ライブラリのPandas、可視化ライブラリのMatplotlibとSeabornを使用して箱ひげ図を作成します。箱ひげ図は、データセット内の数値データの分布や中央値、四分位数、外れ値を視覚的に表現します。

## インストール方法

1. このリポジトリをクローンします。

   ```bash
   git clone https://github.com/yourusername/boxplot-project.git
   ```

2. Pythonの仮想環境を作成します（オプション）。

   ```bash
   cd boxplot-project
   python -m venv venv
   ```

3. 仮想環境をアクティブにします。

   - Windows:

     ```bash
     venv\Scripts\activate
     ```

   - macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. 必要なライブラリをインストールします。

   ```bash
   pip install pandas matplotlib seaborn streamlit
   ```

## 使い方

1. プロジェクトのディレクトリに移動します。

   ```bash
   cd boxplot-project
   ```

2. `app.py` を実行してStreamlitアプリケーションを起動します。

   ```bash
   streamlit run app.py
   ```

3. ブラウザで表示されるURLにアクセスし、アップロードボタンからCSVファイルをアップロードします。

4. アップロードされたデータを箱ひげ図として表示します。

5. 箱ひげ図の見た目をカスタマイズしたい場合は、`app.py` ファイルを編集してください。

## 注意事項

- CSVファイルのデータ構造は、1列目がグループ名、2列目が数値データである必要があります。
- 外れ値の除去は、1.5 * IQR（四分位範囲）を基準に行われます。

このプロジェクトを使用することで、Pythonを使った効率的な箱ひげ図の作成方法を学ぶことができます。データ分析や可視化の際に役立つツールとして活用してください。

---

このREADMEファイルをプロジェクトのルートディレクトリに `README.md` という名前で保存し、プロジェクトの説明や使い方をまとめてください。これにより、他の人がプロジェクトを理解し、使い方を把握するのに役立ちます。
