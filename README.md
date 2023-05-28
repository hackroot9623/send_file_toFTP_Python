# FTP File Uploader
## send_file_toFTP_Python

This script uploads files from a local directory to a remote FTP server. It uses the `ftplib` module in Python to establish an FTP connection and transfer files.

## Prerequisites

- Python 3.x
- `ftplib` module (usually comes bundled with Python)
- Internet connection to connect to the FTP server

## Getting Started

1. Clone or download this repository to your local machine.

2. Install the required dependencies, if any, by running the following command:
  ```bash
  pip install ftplib
  ```
3. Open the `upload_files.py` file and provide the necessary FTP server credentials and file paths:
- Set the `ftp_host` variable to the hostname or IP address of the FTP server.
- Set the `ftp_user` variable to the username for the FTP server.
- Set the `ftp_pass` variable to the password for the FTP server.
- Set the `local_dir` variable to the local directory path containing the files you want to upload.
- Set the `remote_dir` variable to the remote directory path on the FTP server where you want to upload the files.

4. Save the changes to the `upload_files.py` file.

5. Run the script by executing the following command:
  ```bash
  python main.py
  ```

6. The script will connect to the FTP server, navigate to the remote directory, and upload the files from the local directory.

7. After the upload is complete, the script will verify if all files were uploaded successfully and display an appropriate message.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and use this script according to your requirements.

## Disclaimer

Please use this script responsibly and ensure that you have the necessary permissions to access and upload files to the FTP server.

## Contributions

Contributions, issues, and feature requests are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## Contact

If you have any questions, feel free to reach out:

- [Email](mailto:eliser.santiesteban.1996@gmail.com)
- [Twitter](https://twitter.com/hackroot231)

