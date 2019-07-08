import glob
import os
import datetime
from send2trash import send2trash

root_dir="D:\Tutorials\spring-hibernate-tutorial"
target_date = datetime.date(2018,5,18)
# =============================================================================
# for filename in glob.iglob(root_dir + '**/*', recursive=True):
#     if (filename.endswith("-it.srt") or filename.endswith("-tr.srt")): 
#         print(filename)
#         send2trash(filename)
# =============================================================================

# =============================================================================
# for filename in glob.iglob(root_dir +"**/*/*" , recursive=True):
#         m_datetime = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
#         m_date = m_datetime.date()
#         if m_date == target_date:
#             print(filename +" : " + str(m_date))
#             send2trash(filename)
# =============================================================================



