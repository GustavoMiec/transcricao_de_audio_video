# Transcrição de Áudio e Vídeo com Python 🎧📝

Este repositório contém **scripts em Python** para:
- Transcrever arquivos de **áudio (.wav)** para texto
- Extrair o áudio de um **vídeo (.mp4)** e depois realizar a transcrição

A transcrição é feita utilizando a biblioteca **SpeechRecognition** com o serviço **Google Speech Recognition**.

---

## ✅ Funcionalidades

### 1) Transcrição de áudio (`audio_to_text.py`)
- Lê um arquivo `audio.wav`
- Converte a fala em texto (PT-BR)
- Salva o resultado em um arquivo `.txt`

Arquivo gerado:
- `transcription1.txt`

---

### 2) Vídeo → Áudio → Texto (`video_to_text.py`)
- Extrai o áudio de um vídeo (`video.mp4`)
- Salva o áudio como `audio.wav`
- Transcreve o áudio para texto
- Salva o resultado em um arquivo `.txt`

Arquivo gerado:
- `transcription.txt`

---

## 🧩 Tecnologias / Bibliotecas

- Python
- `speechrecognition`
- `moviepy`

> O serviço de transcrição utilizado é o **Google Speech Recognition** (gratuito, mas com limitações).

---

## 📁 Estrutura sugerida do projeto

```text
.
├─ audio.wav
├─ video.mp4
├─ audio_to_text.py
├─ video_to_text.py
└─ README.md
```

---

## ⚙️ Instalação

Instale as dependências com:

```bash
pip install SpeechRecognition moviepy
```

> Em alguns sistemas, pode ser necessário instalar também:
```bash
pip install pyaudio
```

---

## ▶️ Como usar

### Transcrever apenas áudio
```bash
python audio_to_text.py
```

### Transcrever vídeo
```bash
python video_to_text.py
```

Certifique-se de que:
- O arquivo `audio.wav` ou `video.mp4` esteja na mesma pasta do script
- O áudio esteja em um formato compatível (PCM WAV funciona melhor)

---

## 📝 Observações importantes

- O reconhecimento funciona melhor com **áudios limpos**, sem muito ruído
- O idioma está configurado como **pt-BR**
- Áudios longos podem falhar, pois o serviço do Google possui limites

---

## 🛟 Possíveis erros

### `speech_recognition.RequestError`
- Sem conexão com a internet
- Limite do serviço gratuito atingido

### `speech_recognition.UnknownValueError`
- Áudio com baixa qualidade
- Fala muito rápida ou ruído excessivo

---

## 📌 Ideias de melhorias

- [ ] Dividir o áudio em chunks para áudios longos
- [ ] Adicionar suporte a outros idiomas
- [ ] Usar Whisper (OpenAI) para maior precisão
- [ ] Criar interface simples com Streamlit

---

## 🔒 Uso responsável

Evite transcrever áudios de terceiros sem autorização.  
Respeite privacidade e legislação vigente (LGPD).

---

## 📜 Licença

Uso livre para fins educacionais.
