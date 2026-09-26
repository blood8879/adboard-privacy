"""AdBoard 소개 페이지·개인정보처리방침(5개 언어) 생성기.

사용: python3 _build/build.py   (저장소 루트에서)

- /<lang>/index.html      앱 소개(홈페이지). OAuth 검증용 홈페이지는 /en/ 이다.
- /<lang>/privacy.html    개인정보처리방침. 단 한국어는 기존 URL을 지키려고 루트
                          /index.html 에 둔다 — Play Console·OAuth 동의 화면에 이미
                          등록된 주소다.
_build/ 는 밑줄 폴더라 GitHub Pages(Jekyll)가 게시하지 않는다.
"""
from __future__ import annotations

import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://blood8879.github.io/adboard-privacy'
PLAY = 'https://play.google.com/store/apps/details?id=com.seolasoft.adboard'
CONTACT = 'seolasoft@gmail.com'
EFFECTIVE = '2026-09-26'
LANGS = ['en', 'ko', 'ja', 'zh', 'es']
LANG_NAME = {'en': 'English', 'ko': '한국어', 'ja': '日本語', 'zh': '简体中文', 'es': 'Español'}
HTML_LANG = {'en': 'en', 'ko': 'ko', 'ja': 'ja', 'zh': 'zh-Hans', 'es': 'es'}
PLAY_HL = {'en': 'en', 'ko': 'ko', 'ja': 'ja', 'zh': 'zh-CN', 'es': 'es'}
LIMITED_USE_URL = 'https://developers.google.com/terms/api-services-user-data-policy'


def home_path(lang: str) -> str:
    return f'{lang}/index.html'


def privacy_path(lang: str) -> str:
    return 'index.html' if lang == 'ko' else f'{lang}/privacy.html'


def url(path: str) -> str:
    return f'{SITE}/' + path.replace('index.html', '')


def rel(from_path: str, to_path: str) -> str:
    """같은 사이트 안의 상대 링크. index.html 은 폴더 주소로 줄인다."""
    rp = os.path.relpath(to_path, os.path.dirname(from_path) or '.')
    if rp.endswith('index.html'):
        rp = rp[: -len('index.html')] or './'
    return rp


# ───────────────────────── 문구 ─────────────────────────
# 제품 사실(스코프, 로컬 저장, 광고·애널리틱스 SDK, 환율 출처)은 앱 코드 기준이다.
T = {
'en': dict(
  title='AdBoard — AdMob & AdSense earnings dashboard',
  desc='See your AdMob and AdSense earnings at a glance: today, forecast, and share by app, country and more. Read-only access, data stays on your device.',
  eyebrow='For AdMob & AdSense publishers',
  h1='Your ad earnings, at a glance.',
  lead="AdBoard turns your AdMob and AdSense reports into a clear phone dashboard — today's earnings, a 7-day forecast and where your revenue comes from.",
  cta='Get it on Google Play', sub_cta='Free · Android',
  mock_note='Illustration. Figures are examples.',
  apps=['Word Puzzle', 'Step Counter', 'Recipe Box'], other='Other',
  feat_h='Everything you check every day', feat_intro='Built around the questions publishers actually ask.',
  feats=[
    ('chart', 'Clear daily dashboard', "Today, yesterday, this month and last month — each compared with a fair baseline, plus impressions, eCPM, requests and match rate."),
    ('spark', 'Explainable forecast', 'A 7-day forecast from weekday averages. Tap it to see exactly how it was calculated.'),
    ('pie', 'Where revenue comes from', 'Share by ad unit, app, country, format, platform, ad network and mediation group, as a donut or a sortable table.'),
    ('cal', 'Earnings calendar', 'Daily earnings on a calendar with monthly total, daily average and best day; tap any day for its per-app breakdown.'),
    ('users', 'All your accounts', 'Connect AdMob and AdSense publishers from several Google accounts, see AdSense earnings by domain, and view all accounts combined.'),
    ('bell', 'Report, widget, currency', 'Optional 9 AM daily report, a home screen widget, and a secondary currency next to USD (29 currencies, ECB rates).'),
  ],
  priv_h='Privacy by design',
  priv=[
    'Requests <strong>read-only</strong> Google scopes only: <code>admob.readonly</code> and <code>adsense.readonly</code>.',
    'Earnings data and sign-in information are stored <strong>only on your device</strong>. There is no AdBoard server.',
    'Never asks for permission to change ad settings or serve ads.',
  ],
  priv_link='Read the privacy policy',
  lang_h='Available in',
  footer_contact='Contact', footer_privacy='Privacy policy',
  disclaimer='AdBoard is not affiliated with or endorsed by Google. AdMob and AdSense are trademarks of Google LLC.',
  limited_use=f'AdBoard\'s use and transfer to any other app of information received from Google APIs will adhere to the <a href="{LIMITED_USE_URL}">Google API Services User Data Policy</a>, including the Limited Use requirements.',
),
'ko': dict(
  title='AdBoard — 애드몹·애드센스 수익 대시보드',
  desc='AdMob·AdSense 수익을 한눈에. 오늘 수익, 예상 수입, 앱·국가별 비중까지. 읽기 전용 권한, 데이터는 기기에만 저장됩니다.',
  eyebrow='AdMob · AdSense 퍼블리셔를 위한 앱',
  h1='광고 수익을 한눈에.',
  lead='AdBoard는 AdMob·AdSense 리포트를 휴대폰용 대시보드로 보여줍니다. 오늘 수익, 향후 7일 예상 수입, 수익이 어디서 나오는지까지.',
  cta='Google Play에서 받기', sub_cta='무료 · Android',
  mock_note='화면 예시입니다. 수치는 예시입니다.',
  apps=['단어 퍼즐', '만보기', '레시피 노트'], other='기타',
  feat_h='매일 확인하는 것들을 한 곳에', feat_intro='퍼블리셔가 실제로 궁금해하는 질문을 기준으로 만들었습니다.',
  feats=[
    ('chart', '한눈에 보는 대시보드', '오늘 · 어제 · 이번 달 · 지난달 수익을 공정한 기준과 비교해 보여주고, 노출수 · eCPM · 요청수 · 일치율도 함께 봅니다.'),
    ('spark', '근거가 보이는 예상 수입', '요일별 평균으로 향후 7일 수입을 예측합니다. 탭하면 어떻게 계산했는지 그대로 보여줍니다.'),
    ('pie', '수익이 나오는 곳', '광고 단위 · 앱 · 국가 · 포맷 · 플랫폼 · 광고 네트워크 · 미디에이션 그룹별 비중을 도넛 차트나 정렬 가능한 표로 봅니다.'),
    ('cal', '수익 캘린더', '달력으로 보는 일별 수익과 월 합계 · 일평균 · 최고 수익일. 날짜를 누르면 그날의 앱별 내역이 나옵니다.'),
    ('users', '여러 계정을 한 번에', '여러 Google 계정의 AdMob · AdSense 퍼블리셔를 연결하고, AdSense 도메인별 수익과 전체 계정 합산을 봅니다.'),
    ('bell', '리포트 · 위젯 · 통화', '매일 오전 9시 리포트 알림(선택), 홈 화면 위젯, USD 옆에 보조 통화 표시(29개 통화, 유럽중앙은행 환율).'),
  ],
  priv_h='개인정보를 먼저 생각합니다',
  priv=[
    'Google 계정에는 <strong>읽기 전용</strong> 권한 <code>admob.readonly</code>, <code>adsense.readonly</code>만 요청합니다.',
    '수익 데이터와 로그인 정보는 <strong>기기에만</strong> 저장됩니다. AdBoard 서버는 없습니다.',
    '광고 설정을 바꾸거나 광고를 게재하는 권한은 요청하지 않습니다.',
  ],
  priv_link='개인정보처리방침 보기',
  lang_h='지원 언어',
  footer_contact='문의', footer_privacy='개인정보처리방침',
  disclaimer='AdBoard는 Google과 제휴하거나 Google의 보증을 받은 앱이 아닙니다. AdMob과 AdSense는 Google LLC의 상표입니다.',
  limited_use=f'AdBoard가 Google API로부터 받은 정보를 사용하고 다른 앱으로 전송하는 방식은 제한적 사용(Limited Use) 요구사항을 포함한 <a href="{LIMITED_USE_URL}">Google API 서비스 사용자 데이터 정책</a>을 준수합니다.',
),
'ja': dict(
  title='AdBoard — AdMob・AdSense 収益ダッシュボード',
  desc='AdMob・AdSenseの収益をひと目で。今日の収益、収益予測、アプリ・国別の内訳まで。読み取り専用の権限で、データは端末内にのみ保存されます。',
  eyebrow='AdMob・AdSense パブリッシャー向け',
  h1='広告収益を、ひと目で。',
  lead='AdBoardはAdMob・AdSenseのレポートを、スマートフォン向けのわかりやすいダッシュボードにします。今日の収益、今後7日間の予測、収益の出どころまで。',
  cta='Google Play で手に入れよう', sub_cta='無料 · Android',
  mock_note='画面はイメージです。数値は例です。',
  apps=['単語パズル', '歩数計', 'レシピ帳'], other='その他',
  feat_h='毎日チェックすることを、ひとつの画面に', feat_intro='パブリッシャーが本当に知りたいことを基準に作りました。',
  feats=[
    ('chart', 'わかりやすいダッシュボード', '今日・昨日・今月・先月の収益を公平な基準と比較し、表示回数・eCPM・リクエスト数・マッチ率もあわせて確認できます。'),
    ('spark', '根拠が見える収益予測', '曜日別平均から今後7日間の収益を予測。タップすると計算方法をそのまま表示します。'),
    ('pie', '収益の出どころ', '広告ユニット・アプリ・国・フォーマット・プラットフォーム・広告ネットワーク・メディエーショングループ別の割合を、ドーナツチャートや並べ替えできる表で。'),
    ('cal', '収益カレンダー', 'カレンダーで日別収益と月合計・日平均・最高収益日を確認。日付をタップするとアプリ別の内訳が見られます。'),
    ('users', '複数アカウントをまとめて', '複数のGoogleアカウントのAdMob・AdSenseパブリッシャーを連携し、AdSenseのドメイン別収益や全アカウント合算も確認できます。'),
    ('bell', 'レポート・ウィジェット・通貨', '毎朝9時のレポート通知(任意)、ホーム画面ウィジェット、USDの横に補助通貨を表示(29通貨、欧州中央銀行レート)。'),
  ],
  priv_h='プライバシー重視の設計',
  priv=[
    'Googleアカウントには<strong>読み取り専用</strong>の権限 <code>admob.readonly</code>、<code>adsense.readonly</code> のみを要求します。',
    '収益データとログイン情報は<strong>端末内にのみ</strong>保存されます。AdBoardのサーバーはありません。',
    '広告設定の変更や広告配信の権限は要求しません。',
  ],
  priv_link='プライバシーポリシーを読む',
  lang_h='対応言語',
  footer_contact='お問い合わせ', footer_privacy='プライバシーポリシー',
  disclaimer='AdBoardはGoogleと提携しておらず、Googleの承認を受けたアプリではありません。AdMobおよびAdSenseはGoogle LLCの商標です。',
  limited_use=f'AdBoardによるGoogle APIから受け取った情報の使用および他のアプリへの転送は、限定使用(Limited Use)の要件を含む<a href="{LIMITED_USE_URL}">Google API サービスのユーザーデータに関するポリシー</a>に準拠します。',
),
'zh': dict(
  title='AdBoard — AdMob 与 AdSense 收益仪表盘',
  desc='一眼看清 AdMob 和 AdSense 收益:今日收益、收益预测,以及按应用、国家等维度的占比。只读权限,数据只保存在您的设备上。',
  eyebrow='为 AdMob 与 AdSense 发布商打造',
  h1='广告收益,一目了然。',
  lead='AdBoard 把 AdMob 和 AdSense 报告变成清晰的手机仪表盘:今日收益、未来 7 天预测,以及收益来自哪里。',
  cta='在 Google Play 下载', sub_cta='免费 · Android',
  mock_note='界面示意,数字仅为示例。',
  apps=['单词拼图', '计步器', '菜谱本'], other='其他',
  feat_h='每天要看的,都在这里', feat_intro='围绕发布商真正关心的问题设计。',
  feats=[
    ('chart', '清晰的仪表盘', '今日、昨日、本月、上月收益,并与合理的基准对比;同时查看展示次数、eCPM、请求数和匹配率。'),
    ('spark', '有依据的收益预测', '基于星期平均值预测未来 7 天收益。点按即可查看具体计算方式。'),
    ('pie', '收益从哪里来', '按广告单元、应用、国家/地区、格式、平台、广告来源和中介组查看占比,可用环形图或可排序的表格。'),
    ('cal', '收益日历', '在日历上查看每日收益及月度合计、日均收益和最高收益日;点按日期查看当天各应用明细。'),
    ('users', '多账号统一查看', '关联多个 Google 账号下的 AdMob 和 AdSense 发布商,查看 AdSense 按域名收益和全部账号汇总。'),
    ('bell', '报告、小组件、货币', '每天上午 9 点收益报告(可选)、桌面小组件,以及在 USD 旁显示辅助货币(29 种货币,欧洲央行汇率)。'),
  ],
  priv_h='隐私优先的设计',
  priv=[
    '仅向 Google 账号申请<strong>只读</strong>权限:<code>admob.readonly</code> 和 <code>adsense.readonly</code>。',
    '收益数据和登录信息<strong>只保存在您的设备上</strong>。AdBoard 没有服务器。',
    '不会申请更改广告设置或投放广告的权限。',
  ],
  priv_link='阅读隐私政策',
  lang_h='支持语言',
  footer_contact='联系我们', footer_privacy='隐私政策',
  disclaimer='AdBoard 与 Google 无关联,也未获得 Google 认可。AdMob 和 AdSense 是 Google LLC 的商标。',
  limited_use=f'AdBoard 对从 Google API 获得的信息的使用及向其他应用的传输,将遵守 <a href="{LIMITED_USE_URL}">Google API 服务用户数据政策</a>,包括其中的有限使用(Limited Use)要求。',
),
'es': dict(
  title='AdBoard — Panel de ingresos de AdMob y AdSense',
  desc='Tus ingresos de AdMob y AdSense de un vistazo: hoy, previsión y reparto por app, país y más. Acceso de solo lectura; los datos se quedan en tu dispositivo.',
  eyebrow='Para editores de AdMob y AdSense',
  h1='Tus ingresos publicitarios, de un vistazo.',
  lead='AdBoard convierte tus informes de AdMob y AdSense en un panel claro para el móvil: ingresos de hoy, previsión a 7 días y de dónde vienen tus ingresos.',
  cta='Disponible en Google Play', sub_cta='Gratis · Android',
  mock_note='Ilustración. Las cifras son de ejemplo.',
  apps=['Sopa de letras', 'Podómetro', 'Recetario'], other='Otros',
  feat_h='Todo lo que miras cada día', feat_intro='Diseñada en torno a las preguntas que de verdad se hacen los editores.',
  feats=[
    ('chart', 'Panel claro', 'Hoy, ayer, este mes y el mes pasado, cada uno comparado con una referencia justa, además de impresiones, eCPM, solicitudes y tasa de coincidencia.'),
    ('spark', 'Previsión explicable', 'Previsión a 7 días basada en la media de cada día de la semana. Tócala para ver exactamente cómo se calculó.'),
    ('pie', 'De dónde vienen los ingresos', 'Reparto por bloque de anuncios, app, país, formato, plataforma, red publicitaria y grupo de mediación, en anillo o en tabla ordenable.'),
    ('cal', 'Calendario de ingresos', 'Ingresos diarios en un calendario con total mensual, media diaria y mejor día; toca un día para ver su desglose por app.'),
    ('users', 'Todas tus cuentas', 'Conecta editores de AdMob y AdSense de varias cuentas de Google, consulta los ingresos de AdSense por dominio y la vista combinada.'),
    ('bell', 'Informe, widget y moneda', 'Informe diario opcional a las 9:00, widget de pantalla de inicio y moneda secundaria junto al USD (29 monedas, tipos del BCE).'),
  ],
  priv_h='Privacidad desde el diseño',
  priv=[
    'Solo pide permisos de Google de <strong>solo lectura</strong>: <code>admob.readonly</code> y <code>adsense.readonly</code>.',
    'Los datos de ingresos y la información de inicio de sesión se guardan <strong>solo en tu dispositivo</strong>. AdBoard no tiene servidor.',
    'Nunca pide permiso para cambiar la configuración de anuncios ni para publicarlos.',
  ],
  priv_link='Leer la política de privacidad',
  lang_h='Disponible en',
  footer_contact='Contacto', footer_privacy='Política de privacidad',
  disclaimer='AdBoard no está afiliada a Google ni cuenta con su respaldo. AdMob y AdSense son marcas comerciales de Google LLC.',
  limited_use=f'El uso y la transferencia a cualquier otra app, por parte de AdBoard, de la información recibida de las API de Google cumplirán la <a href="{LIMITED_USE_URL}">Política de datos de usuario de los servicios de API de Google</a>, incluidos los requisitos de uso limitado.',
),
}

# 목업 카드 라벨은 앱 ARB와 같은 문구를 쓴다(앱 화면과 똑같이 보이게).
MOCK = {
  'en': dict(dash='Dashboard', today="Today's earnings", so_far='So far', yday="Yesterday's earnings", vs_wk='vs same day last week', fc='Forecast', next7='Next 7 days', share='Earnings share', by_app='App'),
  'ko': dict(dash='대시보드', today='오늘 수익', so_far='현재까지', yday='어제 수익', vs_wk='vs 지난주 같은 요일', fc='예상 수입', next7='향후 7일', share='수익 비중', by_app='앱'),
  'ja': dict(dash='ダッシュボード', today='今日の収益', so_far='現時点まで', yday='昨日の収益', vs_wk='先週の同じ曜日比', fc='収益予測', next7='今後7日間', share='収益の内訳', by_app='アプリ'),
  'zh': dict(dash='仪表盘', today='今日收益', so_far='截至目前', yday='昨日收益', vs_wk='对比上周同日', fc='预计收益', next7='未来7天', share='收益占比', by_app='应用'),
  'es': dict(dash='Panel', today='Ingresos de hoy', so_far='Hasta ahora', yday='Ingresos de ayer', vs_wk='vs mismo día sem. pasada', fc='Previsión', next7='Próximos 7 días', share='Distribución de ingresos', by_app='App'),
}

# ───────────────────── 개인정보처리방침 ─────────────────────
# 각 항목: (제목, 본문 HTML). 사실관계는 모든 언어가 같아야 한다.
P = {
'en': dict(
  title='AdBoard Privacy Policy',
  meta=f'Effective date: {EFFECTIVE}',
  intro='AdBoard ("the app") is an AdMob and AdSense earnings viewer provided by seolasoft ("the developer"). This policy explains what data the app accesses, how it is used, stored and shared, and your choices.',
  sections=[
    ('1. Google user data we access',
     '<p>When you connect a Google account, the app uses Google Sign-In and requests only these <strong>read-only</strong> scopes:</p>'
     '<ul><li><code>https://www.googleapis.com/auth/admob.readonly</code> — to read your AdMob accounts and reports</li>'
     '<li><code>https://www.googleapis.com/auth/adsense.readonly</code> — to read your AdSense accounts and reports</li></ul>'
     '<p>Through these, the app reads publisher account information (publisher ID, account name, time zone, currency) and report data such as earnings, impressions, requests, match rate, eCPM, and the names of apps, ad units, countries, formats, platforms, ad sources, mediation groups and AdSense domains. From Google Sign-In it receives your Google account ID, email address and display name, which are used to label your accounts and keep each publisher with the Google account that owns it.</p>'
     '<p>The app never requests write access and cannot change ad settings, payments or serve ads on your behalf.</p>'),
    ('2. How we use Google user data',
     '<p>Google user data is used <strong>only to show your earnings inside the app</strong> — summaries, statistics, breakdowns, the optional daily notification and the optional home screen widget. It is not used for advertising, is not used to train AI/ML models, and is not sold.</p>'
     f'<p class="note">AdBoard\'s use and transfer to any other app of information received from Google APIs will adhere to the <a href="{LIMITED_USE_URL}">Google API Services User Data Policy</a>, including the Limited Use requirements.</p>'),
    ('3. Where data is stored',
     '<p>All Google user data is stored <strong>only on your device</strong>: report data in the app\'s local database, and the list of connected Google accounts in the operating system\'s secure storage (Android Keystore-backed encrypted storage / iOS Keychain). Sign-in tokens are managed by Google Sign-In on the device. The developer does not operate any server, and Google user data is <strong>never sent to the developer</strong>.</p>'),
    ('4. Sharing',
     '<p>The developer does not share, sell or transfer Google user data to anyone. The app only communicates with Google\'s AdMob and AdSense APIs to fetch your own reports.</p>'),
    ('5. Data collected by third-party services in the app',
     '<p>The app includes the following third-party services. They do <strong>not</strong> receive your AdMob/AdSense report data or Google account information from the app.</p>'
     '<div class="table-scroll"><table><tr><th>Service</th><th>Purpose</th><th>Data it may collect</th></tr>'
     '<tr><td>Google AdMob (Google Mobile Ads SDK)</td><td>Showing ads in the app (banner, app open, rewarded)</td><td>Advertising ID, IP address, device and app information, ad interactions</td></tr>'
     '<tr><td>Google Analytics for Firebase</td><td>Understanding how screens are used to improve the app</td><td>App instance ID, screen views and app events, device model, OS and app version, approximate location derived from IP</td></tr>'
     '<tr><td>Frankfurter exchange rate API (ECB data)</td><td>Showing a secondary currency</td><td>Only the request itself (IP address), no personal data is sent</td></tr></table></div>'
     '<p>These services process data under their own policies: <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a>, <a href="https://policies.google.com/privacy">Google Privacy Policy</a>. You can reset or delete your advertising ID, or opt out of personalized ads, in your device settings.</p>'),
    ('6. Retention and deletion',
     '<ul><li>Disconnecting a publisher in the app deletes that publisher\'s data from the device.</li>'
     '<li>Uninstalling the app deletes all data stored by the app on the device.</li>'
     '<li>You can revoke the app\'s access at any time on your <a href="https://myaccount.google.com/permissions">Google Account permissions page</a>.</li>'
     '<li>Data collected by AdMob and Firebase is retained according to Google\'s policies.</li></ul>'),
    ('7. Children',
     '<p>The app is a tool for advertising publishers and is not directed to children under 13 (or the applicable age in your country).</p>'),
    ('8. Changes to this policy',
     '<p>If this policy changes, the updated version will be posted on this page with a new effective date.</p>'),
    ('9. Contact',
     f'<p>For privacy questions or requests, contact <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>'),
  ],
),
'ko': dict(
  title='AdBoard 개인정보처리방침',
  meta=f'시행일: 2026년 9월 26일 (이전 버전: 2026년 9월 3일)',
  intro='AdBoard(이하 "앱")는 seolasoft(이하 "개발자")가 제공하는 AdMob·AdSense 수익 조회 도구입니다. 본 방침은 앱이 어떤 데이터에 접근하고 어떻게 사용·저장·공유하는지, 그리고 이용자가 선택할 수 있는 사항을 설명합니다.',
  sections=[
    ('1. 접근하는 Google 사용자 데이터',
     '<p>Google 계정을 연결하면 앱은 Google 로그인을 사용하며 다음의 <strong>읽기 전용</strong> 권한만 요청합니다.</p>'
     '<ul><li><code>https://www.googleapis.com/auth/admob.readonly</code> — AdMob 계정 및 리포트 조회</li>'
     '<li><code>https://www.googleapis.com/auth/adsense.readonly</code> — AdSense 계정 및 리포트 조회</li></ul>'
     '<p>이를 통해 퍼블리셔 계정 정보(퍼블리셔 ID, 계정 이름, 시간대, 통화)와 수익 · 노출수 · 요청수 · 일치율 · eCPM 등 리포트 데이터, 그리고 앱 · 광고 단위 · 국가 · 포맷 · 플랫폼 · 광고 소스 · 미디에이션 그룹 · AdSense 도메인 이름을 조회합니다. Google 로그인에서는 Google 계정 ID, 이메일 주소, 표시 이름을 받아 계정을 구분하고 각 퍼블리셔를 소유한 Google 계정과 연결하는 데 사용합니다.</p>'
     '<p>앱은 쓰기 권한을 요청하지 않으며, 광고 설정 · 지급 정보를 변경하거나 광고를 게재할 수 없습니다.</p>'),
    ('2. Google 사용자 데이터의 사용',
     '<p>Google 사용자 데이터는 <strong>앱 화면에 수익을 보여주는 목적으로만</strong> 사용됩니다(요약, 통계, 비중, 선택 시 일일 알림과 홈 화면 위젯). 광고 목적으로 사용하지 않고, AI/ML 모델 학습에 사용하지 않으며, 판매하지 않습니다.</p>'
     f'<p class="note">AdBoard가 Google API로부터 받은 정보를 사용하고 다른 앱으로 전송하는 방식은 제한적 사용(Limited Use) 요구사항을 포함한 <a href="{LIMITED_USE_URL}">Google API 서비스 사용자 데이터 정책</a>을 준수합니다.</p>'),
    ('3. 데이터의 저장',
     '<p>모든 Google 사용자 데이터는 <strong>이용자의 기기에만</strong> 저장됩니다. 리포트 데이터는 앱의 로컬 데이터베이스에, 연결된 Google 계정 목록은 운영체제의 보안 저장소(Android Keystore 기반 암호화 저장소 / iOS Keychain)에 저장되며, 로그인 토큰은 기기의 Google 로그인이 관리합니다. 개발자는 서버를 운영하지 않으며 Google 사용자 데이터를 <strong>개발자에게 전송하지 않습니다</strong>.</p>'),
    ('4. 데이터의 공유',
     '<p>개발자는 Google 사용자 데이터를 누구와도 공유 · 판매 · 이전하지 않습니다. 앱은 이용자 본인의 리포트를 가져오기 위해 Google AdMob · AdSense API와만 통신합니다.</p>'),
    ('5. 앱에 포함된 제3자 서비스가 수집하는 정보',
     '<p>앱에는 다음 제3자 서비스가 포함되어 있습니다. 이 서비스들은 앱으로부터 이용자의 AdMob · AdSense 리포트 데이터나 Google 계정 정보를 <strong>받지 않습니다</strong>.</p>'
     '<div class="table-scroll"><table><tr><th>서비스</th><th>목적</th><th>수집할 수 있는 정보</th></tr>'
     '<tr><td>Google AdMob (Google 모바일 광고 SDK)</td><td>앱 내 광고 표시(배너, 앱 오프닝, 보상형)</td><td>광고 ID, IP 주소, 기기 및 앱 정보, 광고 상호작용</td></tr>'
     '<tr><td>Firebase용 Google 애널리틱스</td><td>화면 이용 현황을 파악해 앱 개선</td><td>앱 인스턴스 ID, 화면 조회 및 앱 이벤트, 기기 모델, OS · 앱 버전, IP 기반 대략적 위치</td></tr>'
     '<tr><td>Frankfurter 환율 API (유럽중앙은행 데이터)</td><td>보조 통화 표시</td><td>요청 자체(IP 주소)만 발생하며 개인정보를 보내지 않음</td></tr></table></div>'
     '<p>이 서비스들은 각자의 정책에 따라 데이터를 처리합니다: <a href="https://policies.google.com/technologies/partner-sites">Google 서비스를 사용하는 사이트 또는 앱의 정보를 Google이 사용하는 방법</a>, <a href="https://policies.google.com/privacy">Google 개인정보처리방침</a>. 광고 ID 재설정 · 삭제나 맞춤 광고 해제는 기기 설정에서 할 수 있습니다.</p>'),
    ('6. 보관 및 삭제',
     '<ul><li>앱에서 퍼블리셔 연결을 해제하면 해당 퍼블리셔의 데이터가 기기에서 삭제됩니다.</li>'
     '<li>앱을 삭제하면 앱이 기기에 저장한 모든 데이터가 삭제됩니다.</li>'
     '<li><a href="https://myaccount.google.com/permissions">Google 계정 권한 페이지</a>에서 언제든 앱의 접근 권한을 철회할 수 있습니다.</li>'
     '<li>AdMob과 Firebase가 수집한 정보는 Google의 정책에 따라 보관됩니다.</li></ul>'),
    ('7. 아동',
     '<p>앱은 광고 퍼블리셔를 위한 도구이며 만 14세 미만(또는 각국 법령상 기준 연령 미만) 아동을 대상으로 하지 않습니다.</p>'),
    ('8. 방침의 변경',
     '<p>본 방침이 변경되면 이 페이지에 새 시행일과 함께 게시합니다.</p>'),
    ('9. 문의',
     f'<p>개인정보 관련 문의 및 요청: <a href="mailto:{CONTACT}">{CONTACT}</a></p>'),
  ],
),
'ja': dict(
  title='AdBoard プライバシーポリシー',
  meta='施行日:2026年9月26日',
  intro='AdBoard(以下「本アプリ」)は、seolasoft(以下「開発者」)が提供するAdMob・AdSense収益閲覧ツールです。本ポリシーでは、本アプリがどのデータにアクセスし、どのように使用・保存・共有するか、また利用者が選択できる事項を説明します。',
  sections=[
    ('1. アクセスするGoogleユーザーデータ',
     '<p>Googleアカウントを連携すると、本アプリはGoogleログインを使用し、次の<strong>読み取り専用</strong>の権限のみを要求します。</p>'
     '<ul><li><code>https://www.googleapis.com/auth/admob.readonly</code> — AdMobアカウントとレポートの取得</li>'
     '<li><code>https://www.googleapis.com/auth/adsense.readonly</code> — AdSenseアカウントとレポートの取得</li></ul>'
     '<p>これにより、パブリッシャーアカウント情報(パブリッシャーID、アカウント名、タイムゾーン、通貨)と、収益・表示回数・リクエスト数・マッチ率・eCPMなどのレポートデータ、ならびにアプリ・広告ユニット・国・フォーマット・プラットフォーム・広告ソース・メディエーショングループ・AdSenseドメインの名前を取得します。Googleログインからは、GoogleアカウントID、メールアドレス、表示名を受け取り、アカウントの識別と、各パブリッシャーを所有するGoogleアカウントとの対応付けに使用します。</p>'
     '<p>本アプリは書き込み権限を要求せず、広告設定や支払い情報の変更、広告の配信を行うことはできません。</p>'),
    ('2. Googleユーザーデータの使用',
     '<p>Googleユーザーデータは<strong>アプリ内で収益を表示する目的にのみ</strong>使用します(サマリー、統計、内訳、任意の日次通知とホーム画面ウィジェット)。広告目的には使用せず、AI/MLモデルの学習にも使用せず、販売もしません。</p>'
     f'<p class="note">AdBoardによるGoogle APIから受け取った情報の使用および他のアプリへの転送は、限定使用(Limited Use)の要件を含む<a href="{LIMITED_USE_URL}">Google API サービスのユーザーデータに関するポリシー</a>に準拠します。</p>'),
    ('3. データの保存',
     '<p>すべてのGoogleユーザーデータは<strong>利用者の端末内にのみ</strong>保存されます。レポートデータはアプリのローカルデータベースに、連携したGoogleアカウントの一覧はOSの安全な保存領域(Android Keystoreベースの暗号化ストレージ / iOSキーチェーン)に保存され、ログイントークンは端末のGoogleログインが管理します。開発者はサーバーを運用しておらず、Googleユーザーデータを<strong>開発者に送信することはありません</strong>。</p>'),
    ('4. データの共有',
     '<p>開発者はGoogleユーザーデータを第三者と共有・販売・移転しません。本アプリは利用者本人のレポートを取得するためにGoogle AdMob・AdSense APIとのみ通信します。</p>'),
    ('5. アプリに含まれる第三者サービスが収集する情報',
     '<p>本アプリには次の第三者サービスが含まれています。これらのサービスは、本アプリから利用者のAdMob・AdSenseレポートデータやGoogleアカウント情報を<strong>受け取りません</strong>。</p>'
     '<div class="table-scroll"><table><tr><th>サービス</th><th>目的</th><th>収集される可能性のある情報</th></tr>'
     '<tr><td>Google AdMob(Google Mobile Ads SDK)</td><td>アプリ内広告の表示(バナー、アプリ起動時、リワード)</td><td>広告ID、IPアドレス、端末・アプリ情報、広告の操作</td></tr>'
     '<tr><td>Google Analytics for Firebase</td><td>画面の利用状況を把握しアプリを改善</td><td>アプリインスタンスID、画面表示とアプリイベント、端末モデル、OS・アプリのバージョン、IPから推定されるおおよその位置</td></tr>'
     '<tr><td>Frankfurter 為替レートAPI(欧州中央銀行データ)</td><td>補助通貨の表示</td><td>リクエスト自体(IPアドレス)のみで、個人情報は送信しません</td></tr></table></div>'
     '<p>これらのサービスはそれぞれのポリシーに従ってデータを処理します:<a href="https://policies.google.com/technologies/partner-sites">Google のサービスを使用するサイトやアプリから収集した情報の Google による使用</a>、<a href="https://policies.google.com/privacy">Google プライバシーポリシー</a>。広告IDのリセット・削除やパーソナライズド広告の無効化は、端末の設定から行えます。</p>'),
    ('6. 保存期間と削除',
     '<ul><li>アプリでパブリッシャーの連携を解除すると、そのパブリッシャーのデータは端末から削除されます。</li>'
     '<li>アプリをアンインストールすると、アプリが端末に保存したすべてのデータが削除されます。</li>'
     '<li><a href="https://myaccount.google.com/permissions">Googleアカウントの権限ページ</a>でいつでもアプリのアクセス権を取り消せます。</li>'
     '<li>AdMobとFirebaseが収集した情報はGoogleのポリシーに従って保存されます。</li></ul>'),
    ('7. 子ども',
     '<p>本アプリは広告パブリッシャー向けのツールであり、13歳未満(またはお住まいの国の法令で定める年齢未満)の子どもを対象としていません。</p>'),
    ('8. 本ポリシーの変更',
     '<p>本ポリシーを変更した場合は、新しい施行日とともにこのページに掲載します。</p>'),
    ('9. お問い合わせ',
     f'<p>プライバシーに関するお問い合わせ・ご請求:<a href="mailto:{CONTACT}">{CONTACT}</a></p>'),
  ],
),
'zh': dict(
  title='AdBoard 隐私政策',
  meta='生效日期:2026 年 9 月 26 日',
  intro='AdBoard(以下简称“本应用”)是由 seolasoft(以下简称“开发者”)提供的 AdMob 和 AdSense 收益查看工具。本政策说明本应用访问哪些数据、如何使用、存储和共享这些数据,以及您可以作出的选择。',
  sections=[
    ('1. 我们访问的 Google 用户数据',
     '<p>当您关联 Google 账号时,本应用使用 Google 登录,并且只申请以下<strong>只读</strong>权限:</p>'
     '<ul><li><code>https://www.googleapis.com/auth/admob.readonly</code> — 读取您的 AdMob 账号和报告</li>'
     '<li><code>https://www.googleapis.com/auth/adsense.readonly</code> — 读取您的 AdSense 账号和报告</li></ul>'
     '<p>通过这些权限,本应用读取发布商账号信息(发布商 ID、账号名称、时区、货币),以及收益、展示次数、请求数、匹配率、eCPM 等报告数据,还有应用、广告单元、国家/地区、格式、平台、广告来源、中介组和 AdSense 域名的名称。通过 Google 登录,本应用获得您的 Google 账号 ID、电子邮件地址和显示名称,用于区分账号,并将每个发布商与其所属的 Google 账号对应。</p>'
     '<p>本应用不申请任何写入权限,无法更改广告设置或付款信息,也无法代您投放广告。</p>'),
    ('2. Google 用户数据的使用',
     '<p>Google 用户数据<strong>仅用于在应用内显示您的收益</strong>(摘要、统计、占比,以及可选的每日通知和桌面小组件)。不会用于广告,不会用于训练 AI/ML 模型,也不会出售。</p>'
     f'<p class="note">AdBoard 对从 Google API 获得的信息的使用及向其他应用的传输,将遵守 <a href="{LIMITED_USE_URL}">Google API 服务用户数据政策</a>,包括其中的有限使用(Limited Use)要求。</p>'),
    ('3. 数据存储位置',
     '<p>所有 Google 用户数据<strong>只保存在您的设备上</strong>:报告数据保存在应用的本地数据库中,已关联的 Google 账号列表保存在操作系统的安全存储中(基于 Android Keystore 的加密存储 / iOS 钥匙串),登录令牌由设备上的 Google 登录管理。开发者不运营任何服务器,Google 用户数据<strong>绝不会发送给开发者</strong>。</p>'),
    ('4. 数据共享',
     '<p>开发者不会与任何人共享、出售或转让 Google 用户数据。本应用仅与 Google AdMob 和 AdSense API 通信,以获取您本人的报告。</p>'),
    ('5. 应用内第三方服务收集的信息',
     '<p>本应用包含以下第三方服务。这些服务<strong>不会</strong>从本应用获得您的 AdMob/AdSense 报告数据或 Google 账号信息。</p>'
     '<div class="table-scroll"><table><tr><th>服务</th><th>用途</th><th>可能收集的信息</th></tr>'
     '<tr><td>Google AdMob(Google 移动广告 SDK)</td><td>在应用内展示广告(横幅、开屏、激励广告)</td><td>广告 ID、IP 地址、设备和应用信息、广告互动</td></tr>'
     '<tr><td>Google Analytics for Firebase</td><td>了解各页面的使用情况以改进应用</td><td>应用实例 ID、页面浏览和应用事件、设备型号、操作系统和应用版本、根据 IP 推断的大致位置</td></tr>'
     '<tr><td>Frankfurter 汇率 API(欧洲央行数据)</td><td>显示辅助货币</td><td>仅产生请求本身(IP 地址),不发送个人信息</td></tr></table></div>'
     '<p>这些服务根据各自的政策处理数据:<a href="https://policies.google.com/technologies/partner-sites">Google 如何使用来自使用其服务的网站或应用的信息</a>、<a href="https://policies.google.com/privacy">Google 隐私权政策</a>。您可以在设备设置中重置或删除广告 ID,或停用个性化广告。</p>'),
    ('6. 保留与删除',
     '<ul><li>在应用中解除某个发布商的关联后,该发布商的数据会从设备上删除。</li>'
     '<li>卸载应用会删除应用在设备上存储的所有数据。</li>'
     '<li>您可以随时在 <a href="https://myaccount.google.com/permissions">Google 账号权限页面</a>撤销本应用的访问权限。</li>'
     '<li>AdMob 和 Firebase 收集的信息按照 Google 的政策保留。</li></ul>'),
    ('7. 儿童',
     '<p>本应用是面向广告发布商的工具,不以 13 周岁以下(或您所在国家/地区法律规定年龄以下)的儿童为对象。</p>'),
    ('8. 政策变更',
     '<p>如本政策发生变更,我们会在此页面发布更新后的版本并注明新的生效日期。</p>'),
    ('9. 联系我们',
     f'<p>如有隐私相关问题或请求,请联系 <a href="mailto:{CONTACT}">{CONTACT}</a>。</p>'),
  ],
),
'es': dict(
  title='Política de privacidad de AdBoard',
  meta='Fecha de entrada en vigor: 26 de septiembre de 2026',
  intro='AdBoard ("la app") es una herramienta para consultar ingresos de AdMob y AdSense proporcionada por seolasoft ("el desarrollador"). Esta política explica a qué datos accede la app, cómo se usan, almacenan y comparten, y qué opciones tienes.',
  sections=[
    ('1. Datos de usuario de Google a los que accedemos',
     '<p>Cuando conectas una cuenta de Google, la app usa el inicio de sesión de Google y solo solicita estos permisos de <strong>solo lectura</strong>:</p>'
     '<ul><li><code>https://www.googleapis.com/auth/admob.readonly</code> — para leer tus cuentas e informes de AdMob</li>'
     '<li><code>https://www.googleapis.com/auth/adsense.readonly</code> — para leer tus cuentas e informes de AdSense</li></ul>'
     '<p>Con ellos, la app lee información de la cuenta de editor (ID de editor, nombre de la cuenta, zona horaria, moneda) y datos de informes como ingresos, impresiones, solicitudes, tasa de coincidencia y eCPM, así como los nombres de apps, bloques de anuncios, países, formatos, plataformas, fuentes de anuncios, grupos de mediación y dominios de AdSense. Del inicio de sesión de Google recibe el ID de tu cuenta de Google, tu correo electrónico y tu nombre visible, que se usan para identificar tus cuentas y asociar cada editor con la cuenta de Google a la que pertenece.</p>'
     '<p>La app nunca solicita permisos de escritura y no puede cambiar la configuración de anuncios ni los pagos, ni publicar anuncios en tu nombre.</p>'),
    ('2. Cómo usamos los datos de usuario de Google',
     '<p>Los datos de usuario de Google se usan <strong>solo para mostrar tus ingresos dentro de la app</strong>: resúmenes, estadísticas, distribuciones, la notificación diaria opcional y el widget opcional. No se usan con fines publicitarios, no se usan para entrenar modelos de IA/ML y no se venden.</p>'
     f'<p class="note">El uso y la transferencia a cualquier otra app, por parte de AdBoard, de la información recibida de las API de Google cumplirán la <a href="{LIMITED_USE_URL}">Política de datos de usuario de los servicios de API de Google</a>, incluidos los requisitos de uso limitado.</p>'),
    ('3. Dónde se almacenan los datos',
     '<p>Todos los datos de usuario de Google se guardan <strong>solo en tu dispositivo</strong>: los datos de informes en la base de datos local de la app y la lista de cuentas de Google conectadas en el almacenamiento seguro del sistema operativo (almacenamiento cifrado respaldado por Android Keystore / Llavero de iOS). Los tokens de inicio de sesión los gestiona el inicio de sesión de Google en el dispositivo. El desarrollador no opera ningún servidor y los datos de usuario de Google <strong>nunca se envían al desarrollador</strong>.</p>'),
    ('4. Cesión de datos',
     '<p>El desarrollador no comparte, vende ni transfiere datos de usuario de Google a nadie. La app solo se comunica con las API de AdMob y AdSense de Google para obtener tus propios informes.</p>'),
    ('5. Datos recogidos por servicios de terceros incluidos en la app',
     '<p>La app incluye los siguientes servicios de terceros. <strong>No</strong> reciben de la app tus datos de informes de AdMob/AdSense ni la información de tu cuenta de Google.</p>'
     '<div class="table-scroll"><table><tr><th>Servicio</th><th>Finalidad</th><th>Datos que puede recoger</th></tr>'
     '<tr><td>Google AdMob (SDK de anuncios de Google para móviles)</td><td>Mostrar anuncios en la app (banner, apertura de app, con recompensa)</td><td>ID de publicidad, dirección IP, información del dispositivo y de la app, interacciones con anuncios</td></tr>'
     '<tr><td>Google Analytics para Firebase</td><td>Entender el uso de las pantallas para mejorar la app</td><td>ID de instancia de la app, vistas de pantalla y eventos, modelo de dispositivo, versión del SO y de la app, ubicación aproximada derivada de la IP</td></tr>'
     '<tr><td>API de tipos de cambio Frankfurter (datos del BCE)</td><td>Mostrar una moneda secundaria</td><td>Solo la propia solicitud (dirección IP); no se envían datos personales</td></tr></table></div>'
     '<p>Estos servicios tratan los datos conforme a sus propias políticas: <a href="https://policies.google.com/technologies/partner-sites">Cómo utiliza Google la información de sitios web o aplicaciones que utilizan sus servicios</a>, <a href="https://policies.google.com/privacy">Política de privacidad de Google</a>. Puedes restablecer o eliminar tu ID de publicidad, o desactivar los anuncios personalizados, en los ajustes del dispositivo.</p>'),
    ('6. Conservación y eliminación',
     '<ul><li>Al desconectar un editor en la app, sus datos se eliminan del dispositivo.</li>'
     '<li>Al desinstalar la app se eliminan todos los datos que la app guardó en el dispositivo.</li>'
     '<li>Puedes revocar el acceso de la app en cualquier momento en la <a href="https://myaccount.google.com/permissions">página de permisos de tu cuenta de Google</a>.</li>'
     '<li>Los datos recogidos por AdMob y Firebase se conservan según las políticas de Google.</li></ul>'),
    ('7. Menores',
     '<p>La app es una herramienta para editores de publicidad y no está dirigida a menores de 14 años (o de la edad aplicable en tu país).</p>'),
    ('8. Cambios en esta política',
     '<p>Si esta política cambia, publicaremos la versión actualizada en esta página con una nueva fecha de entrada en vigor.</p>'),
    ('9. Contacto',
     f'<p>Para consultas o solicitudes sobre privacidad, escribe a <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>'),
  ],
),
}

ICONS = {
  'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2" />',
  'spark': '<path d="M3 17l5-5 4 4 8-9" /><path d="M14 7h6v6" />',
  'pie': '<path d="M12 3v9h9" /><path d="M20.5 15.5A9 9 0 1 1 8.5 3.7" />',
  'cal': '<rect x="3" y="5" width="18" height="16" rx="2" /><path d="M3 10h18M8 3v4M16 3v4" />',
  'users': '<circle cx="9" cy="8" r="3.5" /><path d="M2.5 20a6.5 6.5 0 0 1 13 0" /><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6" />',
  'bell': '<path d="M6 16V11a6 6 0 1 1 12 0v5l2 2H4z" /><path d="M10 21h4" />',
}
PLAY_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M4 2.8v18.4c0 .6.7 1 1.2.7l15.4-9.2c.5-.3.5-1.1 0-1.4L5.2 2.1C4.7 1.8 4 2.2 4 2.8z"/></svg>'


def svg_icon(name: str) -> str:
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def spark(color_var: str, pts: list[float]) -> str:
    w, h = 260, 34
    step = w / (len(pts) - 1)
    lo, hi = min(pts), max(pts)
    ys = [h - 3 - (p - lo) / (hi - lo or 1) * (h - 6) for p in pts]
    d = ' '.join(f'{"M" if i == 0 else "L"}{i * step:.1f},{y:.1f}' for i, y in enumerate(ys))
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" preserveAspectRatio="none" aria-hidden="true">'
            f'<path d="{d}" fill="none" stroke="var({color_var})" stroke-width="2.4" stroke-linejoin="round" /></svg>')


def head(lang: str, path: str, title: str, desc: str, alternates: dict[str, str]) -> str:
    alt = ''.join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url(p)}">' for l, p in alternates.items())
    alt += f'<link rel="alternate" hreflang="x-default" href="{url(alternates["en"])}">'
    css = rel(path, 'assets/site.css')
    icon = rel(path, 'assets/icon-192.png')
    return f'''<!DOCTYPE html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url(path)}">
{alt}
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/assets/icon-512.png">
<meta name="theme-color" content="#0d9488">
<link rel="icon" href="{icon}">
<link rel="stylesheet" href="{css}">
</head>
<body>
'''


def topbar(lang: str, path: str, target) -> str:
    links = ''.join(
        f'<a href="{rel(path, target(l))}" hreflang="{HTML_LANG[l]}" lang="{HTML_LANG[l]}"'
        f'{" aria-current=\"page\"" if l == lang else ""}>{LANG_NAME[l]}</a>'
        for l in LANGS)
    return (f'<header class="top"><div class="wrap">'
            f'<a class="brand" href="{rel(path, home_path(lang))}"><img src="{rel(path, "assets/icon-192.png")}" alt="" width="32" height="32">AdBoard</a>'
            f'<nav class="langs" aria-label="Language">{links}</nav></div></header>\n')


def footer(lang: str, path: str) -> str:
    t = T[lang]
    return f'''<footer><div class="wrap">
<p>{t["limited_use"]}</p>
<p>{t["disclaimer"]}</p>
<p>© 2026 seolasoft · <a href="{rel(path, privacy_path(lang))}">{t["footer_privacy"]}</a> · {t["footer_contact"]}: <a href="mailto:{CONTACT}">{CONTACT}</a></p>
</div></footer>
</body>
</html>
'''


def build_home(lang: str) -> str:
    t, m = T[lang], MOCK[lang]
    path = home_path(lang)
    play = f'{PLAY}&amp;hl={PLAY_HL[lang]}'
    shares = [(t['apps'][0], 46, '#0d9488'), (t['apps'][1], 28, '#f59e0b'), (t['apps'][2], 17, '#8b5cf6'), (t['other'], 9, '#9aa6ae')]
    bar = ''.join(f'<span style="width:{p}%;background:{c}"></span>' for _, p, c in shares)
    legend = ''.join(f'<span><i style="background:{c}"></i>{html.escape(n)} {p}%</span>' for n, p, c in shares)
    feats = ''.join(
        f'<article class="feat"><div class="ico">{svg_icon(ic)}</div><h3>{h}</h3><p>{d}</p></article>'
        for ic, h, d in t['feats'])
    priv = ''.join(f'<li>{p}</li>' for p in t['priv'])
    langs = ''.join(f'<li lang="{HTML_LANG[l]}">{LANG_NAME[l]}</li>' for l in LANGS)
    return head(lang, path, t['title'], t['desc'], {l: home_path(l) for l in LANGS}) + topbar(lang, path, home_path) + f'''<main>
<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">{t["eyebrow"]}</span>
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <a class="cta" href="{play}">{PLAY_ICON}{t["cta"]}</a>
    <span class="sub-cta">{t["sub_cta"]}</span>
  </div>
  <figure class="phone" aria-label="{html.escape(t["mock_note"])}">
    <div class="ph-title">{m["dash"]}</div>
    <div class="mcard"><div class="row"><span class="k amber">{m["today"]}</span><span class="c">{m["so_far"]}</span></div>
      <div class="v">$48.21</div><div class="d up">↗ $3.74 (+8.4%)</div>{spark("--amber", [3, 5, 4, 8, 7, 11, 14])}</div>
    <div class="mcard"><div class="row"><span class="k green">{m["yday"]}</span><span class="c">{m["vs_wk"]}</span></div>
      <div class="v">$52.90</div><div class="d up">↗ $3.04 (+6.1%)</div>{spark("--up", [9, 8, 10, 9, 12, 11, 13])}</div>
    <div class="mcard"><div class="row"><span class="k green">{m["fc"]}</span><span class="c">{m["next7"]}</span></div>
      <div class="v">$356.40</div></div>
    <div class="mcard"><div class="row"><span class="k blue">{m["share"]}</span><span class="c">{m["by_app"]}</span></div>
      <div class="bar">{bar}</div><div class="legend">{legend}</div></div>
    <figcaption class="mock-note">{t["mock_note"]}</figcaption>
  </figure>
</div></section>

<section><div class="wrap">
  <h2>{t["feat_h"]}</h2>
  <p class="intro">{t["feat_intro"]}</p>
  <div class="grid">{feats}</div>
</div></section>

<section><div class="wrap">
  <div class="privacy-box">
    <h2>{t["priv_h"]}</h2>
    <ul>{priv}</ul>
    <a href="{rel(path, privacy_path(lang))}">{t["priv_link"]} →</a>
  </div>
</div></section>

<section><div class="wrap">
  <h2>{t["lang_h"]}</h2>
  <ul class="langs-list">{langs}</ul>
</div></section>
</main>
''' + footer(lang, path)


def build_privacy(lang: str) -> str:
    p = P[lang]
    path = privacy_path(lang)
    body = ''.join(f'<h2>{h}</h2>{b}' for h, b in p['sections'])
    return head(lang, path, p['title'], p['intro'], {l: privacy_path(l) for l in LANGS}) + topbar(lang, path, privacy_path) + f'''<main class="doc"><div class="wrap narrow">
<h1>{p["title"]}</h1>
<p class="meta">{p["meta"]}</p>
<p>{p["intro"]}</p>
{body}
</div></main>
''' + footer(lang, path)



# ── 중국어·일본어 문장부호 정규화 ──
# CJK 글자에 붙은 반각 , : ; ( ) 를 전각으로 바꾼다(중·일 표기 관례).
# 한국어·영어·스페인어에는 적용하지 않는다.
import re as _re  # noqa: E402
_W = '\u3040-\u30ff\u3400-\u9fff\u3000-\u303f\uff00-\uffef\u201c\u201d'
_CJK = _re.compile('[\u3040-\u30ff\u3400-\u9fff]')


def cjk_punct(s):
    def paren(m):
        before, inner = m.group(1), m.group(2)
        if (before and _re.match(f'[{_W}]', before)) or _CJK.search(inner):
            return f'{before}\uff08{inner}\uff09'
        return m.group(0)
    s = _re.sub(r'(.?)\(([^()<>\n]*)\)', paren, s)
    s = _re.sub(f'(?<=[{_W}]) (?=\uff08)', '', s)
    s = _re.sub(f'(?<=[{_W}])([,:;]) ?', lambda m: {',': '\uff0c', ':': '\uff1a', ';': '\uff1b'}[m.group(1)], s)
    return s


def main() -> None:
    for lang in LANGS:
        for path, content in ((home_path(lang), build_home(lang)), (privacy_path(lang), build_privacy(lang))):
            full = os.path.join(ROOT, path)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            if lang in ('zh', 'ja'):
                content = cjk_punct(content)
            with open(full, 'w', encoding='utf-8') as f:
                f.write(content)
            print('wrote', path)


if __name__ == '__main__':
    main()
