from google.cloud import storage
import tempfile

def create_and_upload_file(request):
    # ファイルのコンテンツを作成
    file_content = b'This is the content of the file.'

    # ファイル名とCloud Storageのバケット名を指定
    bucket_name = 'your-bucket-name'  # Cloud Storageのバケット名
    file_name = 'example.txt'

    # Google Cloud Storageクライアントを初期化
    client = storage.Client()

    # ファイルを一時ディレクトリに書き込み
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file_content)

    # ファイルをCloud Storageにアップロード
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(temp_file.name)

    # 一時ファイルを削除
    os.remove(temp_file.name)

    return 'File uploaded to Cloud Storage.'