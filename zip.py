import PySimpleGUI as ui
from zip_creator import make_archive

label1 = ui.Text("select the file to compress:")
input1 = ui.Input()
button1 = ui.FileBrowse("Choose", key="file")

label2 = ui.Text("select the file to compress:")
input2 = ui.Input()
button2 = ui.FolderBrowse("Choose", key='folder')

compress = ui.Button("compress")
output_label = ui.Text(key="output",text_color="green")

window = ui.Window("File compressor", layout=[[label1, input1, button1],[label2, input2, button2],[compress,output_label]])

while True:
    events, values = window.read()
    print(events, values)
    filePath = values['file'].split(';')
    folder = values['folder']
    make_archive(filePath,folder)
    window["output"].update(value="compression_completed")

window.close()
