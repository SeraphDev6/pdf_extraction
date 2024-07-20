from io import BytesIO, StringIO
from pypdf import PdfReader
from urllib.request import Request, urlopen


url = "https://dmv.ca.gov/portal/file/waymo_07022024-pdf"
remoteFile = urlopen(Request(url)).read()
memoryFile = BytesIO(remoteFile)

reader = PdfReader(memoryFile)
