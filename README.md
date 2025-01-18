# Halo GroqBot
## Groq Chat Streamlit App

This [Streamlit](https://streamlit.io/) app integrates with [Groq API](https://console.groq.com) to provide a chat interface where users can interact with advanced language models. It allows users to choose between three models for generating responses, enhancing the flexibility and user experience of the chat application.

## Features

- **Model Selection**: Users can select between `mixtral-8x7b-32768`, `llama2-70b-4096`, and `gemma-7b-it` models to tailor the conversation according to the capabilities of each model.
- **Chat History**: The app maintains a session-based chat history, allowing for a continuous conversation flow during the app session.
- **Dynamic Response Generation**: Utilizes a generator function to stream responses from the Groq API, providing a seamless chat experience.
- **Error Handling**: Implements try-except blocks to gracefully handle potential errors during API calls.

## Requirements

- Streamlit
- Groq Python SDK
- Python 3.7+

## Setup and Installation

- **Install Dependencies**:

  ```bash
  pip install streamlit groq
  ```

- **Set Up Groq API Key**:

  Ensure you have an API key from Groq. This key should be stored securely using Streamlit's secrets management:

  ```toml
  # .streamlit/secrets.toml
  GROQ_API_KEY="your_groq_api_key_here"
  ```

- **Run the App**:
  Navigate to the app's directory and run:

  ```bash
  streamlit run streamlit_app.py
  ```

## Usage

Upon launching the app, you are greeted with a title and a model selection dropdown.

After choosing a preferred model, you can start interacting with the chat interface by entering prompts.

The app displays both the user's questions and the AI's responses, facilitating a back-and-forth conversation.

## Customization

The app can be easily customized to include additional language models (as Groq adds more), alter the user interface, or extend the functionality to incorporate other types of interactions with the Groq API.

## Contributing

Contributions to enhance the app, fix bugs, or improve documentation are welcome.

Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please open an issue or contact the maintainer directly.

## If you"re using Gitgub Secrets, you can set the API key like this:

```bash
mkdir -p .streamlit
echo "[GROQ_API_KEY]" > .streamlit/secrets.toml
echo "value = \"$GROQ_API_KEY\"" >> .streamlit/secrets.toml
```
# Run

```bash
streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
```

# My Streamlit App

Bu proje, kullanıcıların etkileşimli veri görselleştirmeleri oluşturmasına olanak tanıyan bir Streamlit uygulamasıdır.

## Kurulum

Projenin çalışabilmesi için gerekli bağımlılıkları yüklemek için aşağıdaki adımları izleyin:

1. Bu depoyu klonlayın:
   ```
   git clone <repo-url>
   cd my-streamlit-app
   ```

2. Gerekli Python paketlerini yükleyin:
   ```
   pip install -r requirements.txt
   ```

3. Groq API anahtarını ayarlayın:
   ```
   mkdir -p .streamlit
   echo "[GROQ_API_KEY]" > .streamlit/secrets.toml
   echo "value = \"$GROQ_API_KEY\"" >> .streamlit/secrets.toml
   ```

## Kullanım

Uygulamayı başlatmak için aşağıdaki komutu çalıştırın:

```
streamlit run ../../streamlit_app.py
```

Tarayıcınızda otomatik olarak açılacak olan uygulama arayüzü üzerinden etkileşimde bulunabilirsiniz.

## Proje Yapısı

- `src/app.py`: Uygulamanın giriş noktasıdır.
- `src/components/__init__.py`: Uygulamanın bileşenlerini içeren paket.
- `requirements.txt`: Proje için gerekli Python paketlerini listeler.
