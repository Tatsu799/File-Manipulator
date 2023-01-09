# File-Manipulatorの概要
Recursionによるプロジェクト

コマンドとその機能を提供する「file_manipulator.py」というPythonスクリプトを作成する。

・command 'reverse' : python3 reverse inputpath outputpath<br>
   inputpathにあるファイルを受け取り、outputpathにinputpathの内容を逆にして新しいファイルを作成。

・command 'copy' : python3 copy inputpath outputpath<br>
   inputpathのファイルのコピーを作成し、outputpathとして保存する。<br>
   ファイルが存在する場合はエラーを返す。

・command 'duplicate-contents' : python3 duplicate-contents inputpath<br>
   inputpathの内容を読み込み、その内容を複製し複製された内容をinputpathのファイルにn回複製する。

・command 'replace-string' : python3 replace-string inputpath needle newstring <br>
   inputpathの内容から文字列’needle’を検索し、'needle'(文字列)すべてを'newstring'(文字列)に置き換える。
 
