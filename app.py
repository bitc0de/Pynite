from flask import Flask, render_template, request, send_file
from zipfile import ZipFile

app = Flask(__name__)
lista = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global lista
    op1_checked = False
    if request.method == 'POST':
        lista = [request.form.get('chrome'), request.form.get('zoom'), request.form.get('opera'), request.form.get('firefox'),
                 request.form.get('brave'), request.form.get('tor-browser'),request.form.get('utorrent'),request.form.get('qbittorrent'),
                 request.form.get('transmission'),request.form.get('picotorrent'),request.form.get('winrar'),request.form.get('7zip'),
                 request.form.get('peazip'),request.form.get('freearc'),request.form.get('discord'),request.form.get('skype'),
                 request.form.get('pidgin'),request.form.get('thunderbird'),request.form.get('whatsapp'),request.form.get('telegram'),
                 request.form.get('malwarebytes'),request.form.get('avastfreeantivirus'),request.form.get('avginternetsecurity'),
                 request.form.get('spybot'),request.form.get('avirafreeantivirus'),request.form.get('superantispyware'),
                 request.form.get('python'),request.form.get('filezilla'),request.form.get('notepadplusplus'),
                 request.form.get('jdk8'),request.form.get('jdk11'),request.form.get('winscp.portable'),request.form.get('putty'),
                 request.form.get('winmerge'),request.form.get('eclipse'),request.form.get('vscode'),request.form.get('adobereader'),
                 request.form.get('nitroreader.install'),request.form.get('sumatrapdf'),request.form.get('openoffice'),
                 request.form.get('libreoffice-fresh'),request.form.get('teamviewer'),request.form.get('imgburn'),
                 request.form.get('realvnc'),request.form.get('teracopy'),request.form.get('revo-uninstaller'),request.form.get('launchy'),
                 request.form.get('itunes'),request.form.get('itunes'),request.form.get('vlc'),request.form.get('aimp'),
                 request.form.get('winamp'),request.form.get('musicbee'),request.form.get('audacity'),request.form.get('k-litecodecpackfull'),
                 request.form.get('gom-player'),request.form.get('spotify'),request.form.get('cccp'),request.form.get('mediamonkey'),
                 request.form.get('handbrake.portable'),request.form.get('dropbox'),request.form.get('google-backup-and-sync'),
                 request.form.get('googledrive'),request.form.get('netdrive'),request.form.get('sugarsync'),request.form.get('krita'),
                 request.form.get('paint.net'),request.form.get('gimp'),request.form.get('xnview'),request.form.get('inkscape'),
                 request.form.get('sharex'),request.form.get('evernote'),request.form.get('googleearthpro'),
                 request.form.get('keepass'),request.form.get('everithing.portable'),request.form.get('steam'),
                 request.form.get('epicgameslauncher'),request.form.get('battle.net')]
        print (lista)
        return render_template ('update.html')
    return render_template('index.html')

@app.route("/descargar/", methods=['POST'])
def move_forward():
    global lista
    res = []
    for i in lista:
        if i != None:
            res.append(i)
            listprograms = [res]
            print (listprograms)
            with open("source.txt", "w") as f:
                for s in res:
                    f.write(str(s) + "\n")
    return plot_csv()

def plot_csv():
    zipObj = ZipFile('installer.zip', 'w')
    zipObj.write('./source.txt')
    zipObj.write('pynite.exe')
    zipObj.close()
    return send_file('installer.zip',
                     attachment_filename='installer.zip',
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)