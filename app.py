M
My Workspace
My project

Production

hali_whatsapp_bot


Search
Ctrl+
K

New

Upgrade


e
Environment
hali_whatsapp_bot
Events
Settings
Monitor
Logs
Metrics
Manage
Environment
Shell
Scaling
Previews
Disks
Jobs

Changelog
Invite a friend

Contact support
Render Status
Web Service
hali_whatsapp_bot
Python 3
Starter

Connect

Manual Deploy
Service ID:
srv-d3v0566r433s73chkv0g

eliranpv11 / hali_whatsapp_bot
main
https://hali-whatsapp-bot.onrender.com

October 26, 2025 at 1:14 PM
live
ebd535a
Add files via upload

All logs
Search
Search

Live tail
GMT+2

Menu

Collecting flask (from -r requirements.txt (line 1))
  Downloading flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
Collecting twilio (from -r requirements.txt (line 2))
  Downloading twilio-9.8.4-py2.py3-none-any.whl.metadata (13 kB)
Collecting python-dotenv (from -r requirements.txt (line 3))
  Downloading python_dotenv-1.1.1-py3-none-any.whl.metadata (24 kB)
Collecting openai (from -r requirements.txt (line 4))
  Downloading openai-2.6.1-py3-none-any.whl.metadata (29 kB)
Collecting blinker>=1.9.0 (from flask->-r requirements.txt (line 1))
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask->-r requirements.txt (line 1))
  Downloading click-8.3.0-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from flask->-r requirements.txt (line 1))
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask->-r requirements.txt (line 1))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask->-r requirements.txt (line 1))
  Downloading markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting werkzeug>=3.1.0 (from flask->-r requirements.txt (line 1))
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting requests>=2.0.0 (from twilio->-r requirements.txt (line 2))
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting PyJWT<3.0.0,>=2.0.0 (from twilio->-r requirements.txt (line 2))
  Downloading PyJWT-2.10.1-py3-none-any.whl.metadata (4.0 kB)
Collecting aiohttp>=3.8.4 (from twilio->-r requirements.txt (line 2))
  Downloading aiohttp-3.13.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting aiohttp-retry>=2.8.3 (from twilio->-r requirements.txt (line 2))
  Downloading aiohttp_retry-2.9.1-py3-none-any.whl.metadata (8.8 kB)
Collecting anyio<5,>=3.5.0 (from openai->-r requirements.txt (line 4))
  Downloading anyio-4.11.0-py3-none-any.whl.metadata (4.1 kB)
Collecting distro<2,>=1.7.0 (from openai->-r requirements.txt (line 4))
  Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting httpx<1,>=0.23.0 (from openai->-r requirements.txt (line 4))
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting jiter<1,>=0.10.0 (from openai->-r requirements.txt (line 4))
  Downloading jiter-0.11.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.2 kB)
Collecting pydantic<3,>=1.9.0 (from openai->-r requirements.txt (line 4))
  Downloading pydantic-2.12.3-py3-none-any.whl.metadata (87 kB)
Collecting sniffio (from openai->-r requirements.txt (line 4))
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting tqdm>4 (from openai->-r requirements.txt (line 4))
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
Collecting typing-extensions<5,>=4.11 (from openai->-r requirements.txt (line 4))
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting idna>=2.8 (from anyio<5,>=3.5.0->openai->-r requirements.txt (line 4))
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting certifi (from httpx<1,>=0.23.0->openai->-r requirements.txt (line 4))
  Downloading certifi-2025.10.5-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx<1,>=0.23.0->openai->-r requirements.txt (line 4))
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx<1,>=0.23.0->openai->-r requirements.txt (line 4))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic<3,>=1.9.0->openai->-r requirements.txt (line 4))
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.41.4 (from pydantic<3,>=1.9.0->openai->-r requirements.txt (line 4))
  Downloading pydantic_core-2.41.4-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
Collecting typing-inspection>=0.4.2 (from pydantic<3,>=1.9.0->openai->-r requirements.txt (line 4))
  Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 2))
  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 2))
  Downloading aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 2))
  Downloading attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting frozenlist>=1.1.1 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 2))
  Downloading frozenlist-1.8.0-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 2))
  Downloading multidict-6.7.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 2))
  Downloading propcache-0.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 2))
  Downloading yarl-1.22.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (75 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.0.0->twilio->-r requirements.txt (line 2))
  Downloading charset_normalizer-3.4.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
Collecting urllib3<3,>=1.21.1 (from requests>=2.0.0->twilio->-r requirements.txt (line 2))
  Downloading urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Downloading flask-3.1.2-py3-none-any.whl (103 kB)
Downloading twilio-9.8.4-py2.py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 162.7 MB/s eta 0:00:00
Downloading PyJWT-2.10.1-py3-none-any.whl (22 kB)
Downloading python_dotenv-1.1.1-py3-none-any.whl (20 kB)
Downloading openai-2.6.1-py3-none-any.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 147.7 MB/s eta 0:00:00
Downloading anyio-4.11.0-py3-none-any.whl (109 kB)
Downloading distro-1.9.0-py3-none-any.whl (20 kB)
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading jiter-0.11.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (356 kB)
Downloading pydantic-2.12.3-py3-none-any.whl (462 kB)
Downloading pydantic_core-2.41.4-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 176.6 MB/s eta 0:00:00
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading aiohttp-3.13.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 146.0 MB/s eta 0:00:00
Downloading multidict-6.7.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (254 kB)
Downloading yarl-1.22.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (377 kB)
Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Downloading aiohttp_retry-2.9.1-py3-none-any.whl (10.0 kB)
Downloading aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading attrs-25.4.0-py3-none-any.whl (67 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.3.0-py3-none-any.whl (107 kB)
Downloading frozenlist-1.8.0-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (234 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading propcache-0.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (204 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
Downloading certifi-2025.10.5-py3-none-any.whl (163 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
Installing collected packages: urllib3, typing-extensions, tqdm, sniffio, python-dotenv, PyJWT, propcache, multidict, markupsafe, jiter, itsdangerous, idna, h11, frozenlist, distro, click, charset_normalizer, certifi, blinker, attrs, annotated-types, aiohappyeyeballs, yarl, werkzeug, typing-inspection, requests, pydantic-core, jinja2, httpcore, anyio, aiosignal, pydantic, httpx, flask, aiohttp, openai, aiohttp-retry, twilio
Successfully installed PyJWT-2.10.1 aiohappyeyeballs-2.6.1 aiohttp-3.13.1 aiohttp-retry-2.9.1 aiosignal-1.4.0 annotated-types-0.7.0 anyio-4.11.0 attrs-25.4.0 blinker-1.9.0 certifi-2025.10.5 charset_normalizer-3.4.4 click-8.3.0 distro-1.9.0 flask-3.1.2 frozenlist-1.8.0 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.11 itsdangerous-2.2.0 jinja2-3.1.6 jiter-0.11.1 markupsafe-3.0.3 multidict-6.7.0 openai-2.6.1 propcache-0.4.1 pydantic-2.12.3 pydantic-core-2.41.4 python-dotenv-1.1.1 requests-2.32.5 sniffio-1.3.1 tqdm-4.67.1 twilio-9.8.4 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.5.0 werkzeug-3.1.3 yarl-1.22.0
[notice] A new release of pip is available: 25.1.1 -> 25.3
[notice] To update, run: pip install --upgrade pip
==> Uploading build...
==> Uploaded in 10.1s. Compression took 5.6s
==> Build successful 🎉
==> Deploying...
==> Running 'python app.py'
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.217.49.2:5000
Press CTRL+C to quit
127.0.0.1 - - [26/Oct/2025 11:16:05] "HEAD / HTTP/1.1" 404 -
==> New primary port detected: 5000. Restarting deploy to update network configuration...
==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
==> Running 'python app.py'
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.217.49.52:5000
Press CTRL+C to quit
127.0.0.1 - - [26/Oct/2025 11:16:53] "HEAD / HTTP/1.1" 404 -
==> Your service is live 🎉
==> 
==> ///////////////////////////////////////////////////////////
==> 
==> Available at your primary URL https://hali-whatsapp-bot.onrender.com
==> 
==> ///////////////////////////////////////////////////////////
==> Detected a new open port HTTP:5000
==> Detected service running on port 5000
==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
10.217.35.164 - - [26/Oct/2025 11:47:13] "POST /whatsapp HTTP/1.1" 200 -
10.19.114.128 - - [26/Oct/2025 11:48:36] "POST /whatsapp HTTP/1.1" 200 -
Need better ways to work with logs? Try theRender CLI, Render MCP Server, or set up a log stream integration 

0 services selected:

Move

Generate Blueprint

Resume

Suspend

