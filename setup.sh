mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = '#F63366'
backgroundColor = '#FFFFFF'
secondaryBackgroundColor = '#F0F2F6'
textColor = '#262730'
font = 'sans serif'

[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml