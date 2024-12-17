import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from pytube import YouTube
from moviepy.editor import VideoFileClip
import requests
import os
import json

#Idiomas para traduzir em massa
languages = {
    "de": "German",
    "en": "English",
    "es": "Spanish; Castilian",
    "fr": "French",
    "hi": "Hindi",
    "id": "Indonesian",
    "ja": "Japanese",
    "pt": "Portuguese",
    "zh": "Chinese"
}

# Todos os idiomas disponiveis
complete_list_languages = {
  "aa": "Afar",
  "ab": "Abkhazian",
  "ae": "Avestan",
  "af": "Afrikaans",
  "ak": "Akan",
  "am": "Amharic",
  "an": "Aragonese",
  "ar": "Arabic",
  "as": "Assamese",
  "av": "Avaric",
  "ay": "Aymara",
  "az": "Azerbaijani",
  "ba": "Bashkir",
  "be": "Belarusian",
  "bg": "Bulgarian",
  "bh": "Bihari languages",
  "bi": "Bislama",
  "bm": "Bambara",
  "bn": "Bengali",
  "bo": "Tibetan",
  "br": "Breton",
  "bs": "Bosnian",
  "ca": "Catalan; Valencian",
  "ce": "Chechen",
  "ch": "Chamorro",
  "co": "Corsican",
  "cr": "Cree",
  "cs": "Czech",
  "cu": "Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic",
  "cv": "Chuvash",
  "cy": "Welsh",
  "da": "Danish",
  "de": "German",
  "dv": "Divehi; Dhivehi; Maldivian",
  "dz": "Dzongkha",
  "ee": "Ewe",
  "el": "Greek, Modern (1453-)",
  "en": "English",
  "eo": "Esperanto",
  "es": "Spanish; Castilian",
  "et": "Estonian",
  "eu": "Basque",
  "fa": "Persian",
  "ff": "Fulah",
  "fi": "Finnish",
  "fj": "Fijian",
  "fo": "Faroese",
  "fr": "French",
  "fy": "Western Frisian",
  "ga": "Irish",
  "gd": "Gaelic; Scomttish Gaelic",
  "gl": "Galician",
  "gn": "Guarani",
  "gu": "Gujarati",
  "gv": "Manx",
  "ha": "Hausa",
  "he": "Hebrew",
  "hi": "Hindi",
  "ho": "Hiri Motu",
  "hr": "Croatian",
  "ht": "Haitian; Haitian Creole",
  "hu": "Hungarian",
  "hy": "Armenian",
  "hz": "Herero",
  "ia": "Interlingua (International Auxiliary Language Association)",
  "id": "Indonesian",
  "ie": "Interlingue; Occidental",
  "ig": "Igbo",
  "ii": "Sichuan Yi; Nuosu",
  "ik": "Inupiaq",
  "io": "Ido",
  "is": "Icelandic",
  "it": "Italian",
  "iu": "Inuktitut",
  "ja": "Japanese",
  "jv": "Javanese",
  "ka": "Georgian",
  "kg": "Kongo",
  "ki": "Kikuyu; Gikuyu",
  "kj": "Kuanyama; Kwanyama",
  "kk": "Kazakh",
  "kl": "Kalaallisut; Greenlandic",
  "km": "Central Khmer",
  "kn": "Kannada",
  "ko": "Korean",
  "kr": "Kanuri",
  "ks": "Kashmiri",
  "ku": "Kurdish",
  "kv": "Komi",
  "kw": "Cornish",
  "ky": "Kirghiz; Kyrgyz",
  "la": "Latin",
  "lb": "Luxembourgish; Letzeburgesch",
  "lg": "Ganda",
  "li": "Limburgan; Limburger; Limburgish",
  "ln": "Lingala",
  "lo": "Lao",
  "lt": "Lithuanian",
  "lu": "Luba-Katanga",
  "lv": "Latvian",
  "mg": "Malagasy",
  "mh": "Marshallese",
  "mi": "Maori",
  "mk": "Macedonian",
  "ml": "Malayalam",
  "mn": "Mongolian",
  "mr": "Marathi",
  "ms": "Malay",
  "mt": "Maltese",
  "my": "Burmese",
  "na": "Nauru",
  "nb": "Bokmål, Norwegian; Norwegian Bokmål",
  "nd": "Ndebele, North; North Ndebele",
  "ne": "Nepali",
  "ng": "Ndonga",
  "nl": "Dutch; Flemish",
  "nn": "Norwegian Nynorsk; Nynorsk, Norwegian",
  "no": "Norwegian",
  "nr": "Ndebele, South; South Ndebele",
  "nv": "Navajo; Navaho",
  "ny": "Chichewa; Chewa; Nyanja",
  "oc": "Occitan (post 1500)",
  "oj": "Ojibwa",
  "om": "Oromo",
  "or": "Oriya",
  "os": "Ossetian; Ossetic",
  "pa": "Panjabi; Punjabi",
  "pi": "Pali",
  "pl": "Polish",
  "ps": "Pushto; Pashto",
  "pt": "Portuguese",
  "qu": "Quechua",
  "rm": "Romansh",
  "rn": "Rundi",
  "ro": "Romanian; Moldavian; Moldovan",
  "ru": "Russian",
  "rw": "Kinyarwanda",
  "sa": "Sanskrit",
  "sc": "Sardinian",
  "sd": "Sindhi",
  "se": "Northern Sami",
  "sg": "Sango",
  "si": "Sinhala; Sinhalese",
  "sk": "Slovak",
  "sl": "Slovenian",
  "sm": "Samoan",
  "sn": "Shona",
  "so": "Somali",
  "sq": "Albanian",
  "sr": "Serbian",
  "ss": "Swati",
  "st": "Sotho, Southern",
  "su": "Sundanese",
  "sv": "Swedish",
  "sw": "Swahili",
  "ta": "Tamil",
  "te": "Telugu",
  "tg": "Tajik",
  "th": "Thai",
  "ti": "Tigrinya",
  "tk": "Turkmen",
  "tl": "Tagalog",
  "tn": "Tswana",
  "to": "Tonga (Tonga Islands)",
  "tr": "Turkish",
  "ts": "Tsonga",
  "tt": "Tatar",
  "tw": "Twi",
  "ty": "Tahitian",
  "ug": "Uighur; Uyghur",
  "uk": "Ukrainian",
  "ur": "Urdu",
  "uz": "Uzbek",
  "ve": "Venda",
  "vi": "Vietnamese",
  "vo": "Volapük",
  "wa": "Walloon",
  "wo": "Wolof",
  "xh": "Xhosa",
  "yi": "Yiddish",
  "yo": "Yoruba",
  "za": "Zhuang; Chuang",
  "zh": "Chinese",
  "zu": "Zulu"
}
language_select = ""
CONFIG_FILE = 'config_api.json'


# Função para carregar a configuração do arquivo JSON
def load_config():
    if not os.path.exists(CONFIG_FILE):
        # Caso o arquivo não exista, cria um arquivo vazio
        with open(CONFIG_FILE, 'w') as file:
            json.dump({}, file)  # Cria um arquivo vazio com um objeto JSON vazio
        return {}  # Retorna um dicionário vazio caso o arquivo tenha sido criado

    try:
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Caso o arquivo exista, mas tenha conteúdo inválido, retorna um dicionário vazio
        return {}

# Função para salvar a configuração no arquivo JSON
def save_config(data):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Função para baixar vídeo do YouTube e extrair áudio
def baixar_video():
    try:
        video_url = url_entry.get()
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()

        output_path = filedialog.askdirectory()
        if not output_path:
            return

        downloaded_file = stream.download(output_path=output_path)
        audio_file = downloaded_file.rsplit('.', 1)[0] + ".mp3"

        video_clip = VideoFileClip(downloaded_file)
        video_clip.audio.write_audiofile(audio_file)
        video_clip.close()

        messagebox.showinfo("Sucesso", "Áudio extraído com sucesso!")
        enviar_audio_para_transcricao(audio_file)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para enviar o áudio para a API do Whisper (OpenAI)
def enviar_audio_para_transcricao(audio_file):
    openai_api_key = config['openai_api_key']
    if not openai_api_key:
        messagebox.showerror("Erro", "Chave da API do OpenAI não encontrada.")
        return

    url_openai = "https://api.openai.com/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {openai_api_key}"}

    with open(audio_file, "rb") as audio:
        data = {"model": "whisper-1", "response_format": "srt"}
        files = {"file": audio}
        response = requests.post(url_openai, headers=headers, data=data, files=files)

        if response.status_code == 200:
            srt_file = audio_file.replace(".mp3", ".srt")
            with open(srt_file, "w") as f:
                f.write(response.text)
            messagebox.showinfo("Sucesso", "Transcrição criada com sucesso!")
            traduzir_legenda(srt_file)
        else:
            messagebox.showerror("Erro", f"Erro: {response.text}")

# Função para traduzir legenda para vários idiomas usando Google Translate API
def traduzir_legenda(srt_file):
    google_api_key = config['google_api_key']
    if not google_api_key:
        messagebox.showerror("Erro", "Chave da API do Google não encontrada.")
        return

    url_google_translate = (
        f"https://translation.googleapis.com/language/translate/v2?key={google_api_key}"
    )

    with open(srt_file, "r") as file:
        srt_content = file.read()
    if not language_select:
        for lang_code, lang_name in languages.items():
            body = {
                "contents": [srt_content],
                "mimeType": "text/plain",
                "targetLanguageCode": lang_code
            }
            response = requests.post(url_google_translate, headers=headers, json=body)
            if response.status_code == 200:
                translation = response.json().get('translations')[0].get('translatedText')
                translated_srt_file = srt_file.replace(".srt", f"_{lang_name}.srt")
                with open(translated_srt_file, "w") as f:
                    f.write(translation)
                messagebox.showinfo("Sucesso", f"Legenda traduzida para {lang_name}!")
            else:
                messagebox.showerror("Erro", f"Erro ao traduzir para {lang_name}: {response.text}")
    else:
        body = {
            "contents": [srt_content],
            "mimeType": "text/plain",
            "targetLanguageCode": language_select
        }
        response = requests.post(url_google_translate, headers=headers, json=body)
        if response.status_code == 200:
            translation = response.json().get('translations')[0].get('translatedText')
            translated_srt_file = srt_file.replace(".srt", f"_{language_select}.srt")
            with open(translated_srt_file, "w") as f:
                f.write(translation)
            messagebox.showinfo("Sucesso", f"Legenda traduzida para {language_select}!")
        else:
            messagebox.showerror("Erro", f"Erro ao traduzir para {language_select}: {response.text}")

#Função para listar idiomas
def adiciona_lista():    
    listbox.delete(0, tk.END)    
    for lingua in complete_list_languages:        
        listbox.insert(tk.END, f"{lingua} - {complete_list_languages[lingua]}")
        
# Função para enviar o idioma selecionado
def send_selected():
    global language_select  # Permitir acesso à variável global
    selected = listbox.curselection()
    if not selected: #implementar função de criação em massa
        messagebox.showerror("Erro", "Nenhum item selecionado")
        return
    #else:
    index = selected[0]
    lingua = list(listbox.get(index).split(" - "))[0]    
    language_select = lingua  # Define a linguagem selecionada
    baixar_video()
        
# Função para abrir a janela de configuração
def open_config_window():
    config_window = tk.Toplevel(app)
    config_window.title("Configurações")
    config_window.geometry("250x100")  # Tamanho da janela

    tk.Label(config_window, text="Google API Key").grid(row=0, column=0)
    tk.Label(config_window, text="OpenAI Key").grid(row=1, column=0)

    entry_google_api_key = tk.Entry(config_window)
    entry_openai_key = tk.Entry(config_window)

    entry_google_api_key.grid(row=0, column=1)
    entry_openai_key.grid(row=1, column=1)

    entry_google_api_key.insert(0, config.get('google_api_key', ''))
    entry_openai_key.insert(0, config.get('openai_api_key', ''))
    #Fecha janela de configuração
    def exit_btn():
        config_window.destroy()
        config_window.update()
    #Salva e Fecha janela de configuração
    def save_config_and_close():
        new_config = {
            'google_api_key': entry_google_api_key.get(),
            'openai_api_key': entry_openai_key.get(),
        }
        save_config(new_config)
        config_window.destroy()

    tk.Button(config_window, text="Salvar", command=save_config_and_close).grid(row=2, column=0)
    tk.Button(config_window, text="Cancelar", command=exit_btn).grid(row=2, column=1)

# Interface gráfica com Tkinter
app = tk.Tk()
app.title("YouTube Video to Audio Transcription")
var = tk.StringVar()
app.geometry("380x350")  # Tamanho da janela

config = load_config()

tk.Label(app, text="Insira o link do vídeo do YouTube:").grid(row=1, column=0, columnspan=1)

btn_configuracao = tk.Button(app, text="Configurações", command=open_config_window)
btn_configuracao.grid(row=0, column=0)

url_entry = tk.Entry(app, width=50)
url_entry.grid(row=2, column=0)

listbox = tk.Listbox(app)
listbox.grid(row=3, column=0)
adiciona_lista()

download_button = tk.Button(app, text="Baixar, transcrever e traduzir", command=send_selected)
download_button.grid(row=4, column=0)

app.mainloop()
