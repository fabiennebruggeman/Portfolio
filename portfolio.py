import streamlit as st
import streamlit.components.v1 as components
import base64, pathlib
from datetime import datetime

st.set_page_config(
    page_title="Fabienne Louise Bruggeman",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Nuke all chrome and make the iframe fill the screen
st.markdown("""<style>
[data-testid="stHeader"],[data-testid="stToolbar"],
[data-testid="stSidebar"],[data-testid="collapsedControl"],
footer,header{display:none!important;}
html,body,.stApp,[data-testid="stAppViewContainer"],
.block-container,section[data-testid="stMain"],
section[data-testid="stMain"]>div{
  padding:0!important;margin:0!important;max-width:100%!important;
  overflow:hidden!important;background:#008080!important;}
/* Make the iframe fill everything */
.stApp iframe {
  position:fixed!important;
  top:0!important;left:0!important;
  width:100vw!important;height:100vh!important;
  border:none!important;
  z-index:9999!important;
}
</style>""", unsafe_allow_html=True)

def _b64(path):
    p = pathlib.Path(path)
    if p.exists():
        return base64.b64encode(p.read_bytes()).decode()
    return None

BG_B64    = _b64("assets/background.png")   # optional — drop a background.png in assets/ to use it
PHOTO_B64 = _b64("assets/photo.jpeg")
FOLDER_B64 = "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"
now       = datetime.now().strftime("%I:%M %p")

bg_css = (
    f'background:url("data:image/png;base64,{BG_B64}") center/cover no-repeat;'
    if BG_B64 else 'background:#008080;'
)

photo_src = (
    f'data:image/jpeg;base64,{PHOTO_B64}'
    if PHOTO_B64 else ''
)

folder_src = (
    f'data:image/png;base64,{FOLDER_B64}'
    if FOLDER_B64 else ''
)

# Build HTML as a plain string (no f-string for the body, inject values via replace)
HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body{
  width:100vw;height:100vh;overflow:hidden;
  BG_CSS_PLACEHOLDER
  font-family:"MS Sans Serif",Tahoma,Arial,sans-serif;
  font-size:11px;
}
.desktop{
  position:fixed;top:0;left:0;right:0;bottom:28px;
  overflow-y:auto;overflow-x:hidden;
  display:flex;align-items:center;justify-content:center;
  padding:10px 0 6px 0;
}
.deskicons{
  position:absolute;left:5px;top:5px;
  display:flex;flex-direction:column;gap:1px;
}
.deskicon{
  width:80px;padding:4px 2px;
  display:flex;flex-direction:column;align-items:center;
  cursor:default;user-select:none;border:1px solid transparent;
}
.deskicon:hover{background:rgba(0,0,128,.4);border:1px dotted rgba(255,255,255,.6);}
.deskicon.selected{background:rgba(0,0,128,.5);border:1px dotted rgba(255,255,255,.7);}
.di{width:64px;height:64px;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:1px;}
.dl{color:#fff;font-size:11px;text-align:center;line-height:1.3;
  text-shadow:1px 1px 0 #000,-1px 0 0 #000,0 -1px 0 #000,1px 0 0 #000;}
.ctx-item{padding:3px 20px 3px 8px;font-size:11px;cursor:default;white-space:nowrap;}
.ctx-item:hover{background:#000080;color:#fff;}
.ctx-div{height:1px;background:#808080;border-bottom:1px solid #fff;margin:2px 0;}
/* CV window */
.cvwin{
  width:650px;max-width:calc(100vw - 80px);
  background:#c0c0c0;
  border:2px solid;border-color:#ffffff #404040 #404040 #ffffff;
  box-shadow:2px 2px 0 #000;
  margin:auto;
}
/* Title bar */
.titlebar{
  height:18px;
  background:linear-gradient(to right,#000080 0%,#1084d0 100%);
  display:flex;align-items:center;padding:1px 3px;gap:3px;
}
.tb-title{color:#fff;font-size:11px;font-weight:bold;flex:1;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding-left:2px;}
.tb-btns{display:flex;gap:2px;margin-left:4px;}
.tb-btn{width:16px;height:14px;background:#c0c0c0;
  border:1px solid;border-color:#fff #808080 #808080 #fff;
  display:flex;align-items:center;justify-content:center;
  font-size:9px;font-weight:bold;cursor:default;}
/* Menu bar */
.menubar{height:18px;background:#c0c0c0;border-bottom:1px solid #808080;
  display:flex;align-items:center;padding:0 4px;}
.mi{padding:1px 6px;cursor:default;font-size:11px;}
.mi:hover{background:#000080;color:#fff;}
/* Toolbar */
.toolbar{height:23px;background:#c0c0c0;border-bottom:1px solid #808080;
  display:flex;align-items:center;padding:1px 4px;gap:2px;}
.t-btn{height:17px;padding:0 5px;background:#c0c0c0;
  border:1px solid;border-color:#fff #808080 #808080 #fff;
  font-size:10px;cursor:default;white-space:nowrap;}
.t-sep{width:1px;height:15px;background:#808080;
  border-right:1px solid #fff;margin:0 2px;}
/* Address bar */
.addrbar{height:21px;background:#c0c0c0;border-bottom:1px solid #808080;
  display:flex;align-items:center;padding:1px 6px;gap:4px;}
.a-lbl{font-size:11px;font-weight:bold;white-space:nowrap;}
.a-field{flex:1;height:15px;background:#fff;
  border:2px solid;border-color:#808080 #fff #fff #808080;
  padding:0 3px;font-size:11px;color:#00f;
  font-family:"MS Sans Serif",Arial,sans-serif;}
.a-go{height:15px;padding:0 5px;background:#c0c0c0;
  border:1px solid;border-color:#fff #808080 #808080 #fff;
  font-size:10px;cursor:default;}
/* Content */
.content{background:#fff;
  border:2px solid;border-color:#808080 #fff #fff #808080;
  margin:3px;padding:5px;
  display:flex;flex-direction:column;gap:4px;
}
.photo-win{width:130px;flex-shrink:0;
  border:2px solid;border-color:#808080 #fff #fff #808080;background:#000;}
.photo-tb{height:16px;background:linear-gradient(to right,#000080,#1084d0);
  display:flex;align-items:center;padding:0 3px;gap:2px;overflow:hidden;}
.photo-tb-icon{font-size:10px;flex-shrink:0;}
.photo-tb-txt{color:#fff;font-size:10px;font-weight:bold;flex:1;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.photo-tb-x{width:12px;height:12px;background:#c0c0c0;flex-shrink:0;
  border:1px solid;border-color:#fff #808080 #808080 #fff;
  display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:bold;}
.photo-toolbar{height:22px;background:#c0c0c0;border-bottom:1px solid #808080;
  display:flex;align-items:center;padding:0 4px;gap:2px;}
.ph-btn{height:18px;min-width:18px;padding:0 4px;background:#c0c0c0;
  border:2px solid;border-color:#fff #808080 #808080 #fff;
  font-size:10px;cursor:default;display:flex;align-items:center;justify-content:center;
  line-height:1;}
.ph-sep{width:1px;height:14px;background:#808080;border-right:1px solid #fff;margin:0 2px;}
.photo-area{background:#1a1a1a;padding:4px;
  display:flex;align-items:center;justify-content:center;position:relative;}
.photo-area img{
  width:112px;height:140px;
  object-fit:cover;object-position:top center;display:block;
  filter:grayscale(100%) contrast(1.1) brightness(0.92);
  image-rendering:auto;
}
/* scanlines overlay */
.photo-area::after{
  content:"";position:absolute;top:4px;left:4px;
  width:112px;height:140px;
  background:repeating-linear-gradient(
    to bottom,
    transparent 0px,transparent 1px,
    rgba(0,0,0,0.18) 1px,rgba(0,0,0,0.18) 2px
  );
  pointer-events:none;
}
.photo-stat{height:16px;background:#c0c0c0;border-top:1px solid #808080;
  display:flex;align-items:center;padding:0 5px;font-size:9px;gap:6px;
  border-bottom:1px solid #808080;}
.photo-nav{display:flex;align-items:center;justify-content:center;gap:3px;
  padding:3px 4px;background:#c0c0c0;border-top:1px solid #808080;}
.ph-nav-btn{height:18px;min-width:22px;padding:0 4px;background:#c0c0c0;
  border:2px solid;border-color:#fff #808080 #808080 #fff;
  font-size:10px;cursor:default;display:flex;align-items:center;justify-content:center;}
/* Boxes */
.box{border:2px solid;border-color:#808080 #fff #fff #808080;}
.bh{background:#000080;color:#fff;font-size:10px;font-weight:bold;padding:1px 5px;}
.bb{padding:3px 5px;font-size:10px;line-height:1.35;color:#000;background:#fff;}
.bb b{font-weight:bold;}
/* Layout */
.row{display:flex;gap:4px;}
.rpanel{flex:1;display:flex;flex-direction:column;gap:4px;}
.two{display:flex;gap:4px;}
.two>*{flex:1;}
/* right column in row 2: stacks skills + languages */
.rcol{width:185px;flex-shrink:0;display:flex;flex-direction:column;gap:0;}
/* work experience table-style */
.wexp{padding:0!important;}
.wrow{display:flex;gap:0;padding:3px 6px;}
.wrow:nth-child(odd){background:#f8f8f8;}
.wleft{width:190px;flex-shrink:0;font-size:10px;line-height:1.5;
  padding-right:8px;border-right:1px solid #d0d0d0;}
.wright{flex:1;font-size:10px;line-height:1.5;padding-left:8px;}
.wdiv{height:1px;background:#d0d0d0;margin:0 6px;}
/* Status bar */
.statusbar{height:18px;background:#c0c0c0;border-top:1px solid #808080;
  display:flex;align-items:center;padding:0 3px;gap:2px;}
.sp{height:14px;border:2px solid;border-color:#808080 #fff #fff #808080;
  padding:0 5px;display:flex;align-items:center;font-size:10px;}
/* Portfolio window */
.portwin{
  position:absolute;
  top:18px;left:24px;
  width:340px;
  background:#c0c0c0;
  border:2px solid;border-color:#ffffff #404040 #404040 #ffffff;
  box-shadow:2px 2px 0 #000;
  display:none;
  z-index:200;
}
.portwin .titlebar{
  height:18px;
  background:linear-gradient(to right,#000080 0%,#1084d0 100%);
  display:flex;align-items:center;padding:1px 3px;gap:3px;
}
.portwin .tb-title{color:#fff;font-size:11px;font-weight:bold;flex:1;padding-left:2px;}
.portwin .tb-btns{display:flex;gap:2px;margin-left:4px;}
.portwin .tb-btn{width:16px;height:14px;background:#c0c0c0;
  border:1px solid;border-color:#fff #808080 #808080 #fff;
  display:flex;align-items:center;justify-content:center;
  font-size:9px;font-weight:bold;cursor:default;}
.port-tabs{
  display:flex;
  padding:4px 6px 0 6px;
  gap:0;
  position:relative;
  z-index:2;
}
.port-tab{
  padding:3px 18px 3px 18px;
  background:#c0c0c0;
  border:2px solid;
  border-color:#ffffff #808080 #c0c0c0 #ffffff;
  border-bottom:none;
  font-size:11px;
  cursor:pointer;
  margin-right:-1px;
  position:relative;
  top:2px;
  z-index:10;
  font-family:"MS Sans Serif",Tahoma,Arial,sans-serif;
}
.port-tab.active{
  background:#c0c0c0;
  border-color:#ffffff #808080 #c0c0c0 #ffffff;
  z-index:3;
  padding-top:4px;
}
.port-body{
  background:#c0c0c0;
  border:2px solid;border-color:#808080 #ffffff #ffffff #808080;
  margin:0 4px 4px 4px;
  padding:12px 10px;
  font-size:11px;
  position:relative;
  z-index:1;
  min-height:60px;
}

.taskbar{position:fixed;bottom:0;left:0;right:0;height:28px;
  background:#c0c0c0;
  border-top:2px solid;border-color:#fff #808080 #808080 #fff;
  display:flex;align-items:center;padding:2px;gap:2px;z-index:99999;}
.start{height:22px;padding:0 8px;background:#c0c0c0;
  border:2px solid;border-color:#fff #808080 #808080 #fff;
  display:flex;align-items:center;gap:4px;
  font-weight:bold;font-size:11px;cursor:default;}
.tb-div{width:2px;height:20px;
  border-left:1px solid #808080;border-right:1px solid #fff;margin:0 2px;}
.tb-win{height:22px;min-width:130px;padding:0 7px;background:#c0c0c0;
  border:2px solid;border-color:#808080 #fff #fff #808080;
  display:flex;align-items:center;font-size:11px;font-weight:bold;cursor:default;
  white-space:nowrap;box-shadow:1px 1px 0 #999 inset;}
.tb-tray{margin-left:auto;height:22px;
  border:2px solid;border-color:#808080 #fff #fff #808080;
  display:flex;align-items:center;padding:0 8px;font-size:11px;gap:6px;}
</style>
</head>
<body>

<div class="desktop">
  <div class="deskicons">
    <div class="deskicon" id="portfolioIcon" oncontextmenu="showCtxMenu(event)" ondblclick="openPortfolio()" onclick="selectIcon(this)">
      <div class="di"><img src="FOLDER_SRC_PLACEHOLDER" style="width:64px;height:64px;object-fit:contain;image-rendering:pixelated;" alt="folder"/></div>
      <div class="dl" style="margin-top:0;">Portfolio</div>
    </div>
  </div>

  <!-- Right-click context menu -->
  <div id="ctxMenu" style="display:none;position:fixed;z-index:99998;background:#c0c0c0;border:2px solid;border-color:#fff #808080 #808080 #fff;box-shadow:2px 2px 0 #000;min-width:140px;">
    <div class="ctx-item" onclick="openPortfolio();hideCtxMenu();"><b>Open</b></div>
    <div class="ctx-div"></div>
    <div class="ctx-item" onclick="hideCtxMenu()">Get Info</div>
    <div class="ctx-item" onclick="hideCtxMenu()">Copy</div>
    <div class="ctx-item" onclick="hideCtxMenu()">Share...</div>
  </div>

  <!-- Portfolio + CV stacked -->
  <div style="position:relative;display:inline-block;">

    <!-- Portfolio window (shown on dblclick, sits above CV) -->
    <div class="portwin" id="portWin">
      <div class="titlebar">
        
        <div class="tb-title">Portfolio</div>
        <div class="tb-btns">
          <div class="tb-btn">_</div>
          <div class="tb-btn">&#9633;</div>
          <div class="tb-btn" onclick="closePortfolio()"><b>X</b></div>
        </div>
      </div>
      <div class="port-tabs">
        <div class="port-tab active" id="tab-writing" onclick="switchTab('writing')">Writing</div>
        <div class="port-tab" id="tab-developing" onclick="switchTab('developing')">Developing</div>
      </div>
      <div class="port-body">
        <div id="panel-writing">&nbsp;</div>
        <div id="panel-developing" style="display:none;">&nbsp;</div>
      </div>
    </div>

  <div class="cvwin">
    <div class="titlebar">
      <div class="tb-title">Fabienne Bruggeman - CV.htm - Microsoft Internet Explorer</div>
      <div class="tb-btns">
        <div class="tb-btn">_</div>
        <div class="tb-btn">&#9633;</div>
        <div class="tb-btn"><b>X</b></div>
      </div>
    </div>
    <div class="menubar">
      <span class="mi"><u>F</u>ile</span>
      <span class="mi"><u>E</u>dit</span>
      <span class="mi"><u>V</u>iew</span>
      <span class="mi">F<u>a</u>vourites</span>
      <span class="mi"><u>T</u>ools</span>
      <span class="mi"><u>H</u>elp</span>
    </div>
    <div class="toolbar">
      <div class="t-btn">&lt; Back</div>
      <div class="t-btn">Forward &gt;</div>
      <div class="t-sep"></div>
      <div class="t-btn">Stop</div>
      <div class="t-btn">Refresh</div>
      <div class="t-sep"></div>
      <div class="t-btn">Home</div>
      <div class="t-btn">Search</div>
      <div class="t-btn">Favourites</div>
      <div class="t-btn">Print</div>
    </div>
    <div class="addrbar">
      <span class="a-lbl">Address</span>
      <div class="a-field">http://www.fabienne-bruggeman.com/cv.htm</div>
      <div class="a-go">Go</div>
    </div>
    <div class="content">

      <!-- ROW 1: photo + personal details + profile -->
      <div class="row">
        <div class="photo-win">
          <div class="photo-tb">
            
            <span class="photo-tb-txt">Picture.JPEG</span>
            <div class="photo-tb-x">X</div>
          </div>
          <div class="photo-toolbar">
            <div class="ph-btn">&lt;</div>
            <div class="ph-btn">&gt;</div>
            <div class="ph-sep"></div>
            <div class="ph-btn">+</div>
            <div class="ph-btn">&minus;</div>
            <div class="ph-sep"></div>
            <div class="ph-btn">&#9645;</div>
          </div>
          <div class="photo-area">
            <img src="PHOTO_SRC_PLACEHOLDER" alt="Picture.JPEG" />
          </div>
          <div class="photo-stat">
            <span>Picture.JPEG</span>
            <span>1 of 1</span>
          </div>
          <div class="photo-nav">
            <div class="ph-nav-btn">|&lt;</div>
            <div class="ph-nav-btn">&lt;</div>
            <div class="ph-nav-btn">&gt;</div>
            <div class="ph-nav-btn">&gt;|</div>
          </div>
        </div>
        <div class="rpanel">
          <div class="box">
            <div class="bh">Personal Details</div>
            <div class="bb">
              <b>Name:</b> Fabienne Louise Bruggeman &nbsp;|&nbsp;
              <b>DOB:</b> 16 August 2000 &nbsp;|&nbsp;
              <b>Nationality:</b> Dutch<br>
              <b>Location:</b> Aldinga Beach, South Australia<br>
              <b>Email:</b> fabienne.bruggeman@hotmail.com
            </div>
          </div>
          <div class="box">
            <div class="bh">Profile</div>
            <div class="bb">
              As an educator and recent master's graduate of European Studies, I value
              translating this blend of practical expertise and academic discipline in
              results-driven roles. On a personal level, I am driven by the conviction
              that narrative representation functions as a critical mechanism for social
              change. Based on that principle, I have experience as an ESL teacher, a
              student assistant at an educational foundation focused on providing accessible
              education, and as an intern at the Dutch sustainable financial institution
              ASN Bank. I currently operate at the intersection of recruiting and AI
              innovation for Innodata, building bridges across academia and the AI industry to ensure
              that the development of LLMs is guided by expert-led data. I have also
              adopted digital product building (SaaS) as a technical pursuit. Over the
              past years, I have gained experience living in Japan, Australia, Scotland
              and the Netherlands. I am native in Dutch and English, and speak Japanese
              at a conversational level.
            </div>
          </div>
        </div>
      </div>

      <!-- ROW 2: Education (left) | Skills + Languages (right) -->
      <div class="two">
        <div class="box">
          <div class="bh">Education</div>
          <div class="bb">
            <b>MA European Studies</b><br>
            University of Amsterdam &nbsp;|&nbsp; EQF Level 7<br>
            Specialisation in Identity and Integration &#8212; European culture and politics,
            media and identity, race and the state.
            Thesis research at the Black Cultural Archives, London.<br>
            <br>
            <b>BA English Language and Culture</b><br>
            Utrecht University &nbsp;|&nbsp; EQF Level 6<br>
            Specialisation in Intertextuality. Minor in Violence (UvA).
            Semester abroad at Kyoto University. Communications internship
            at ASN&nbsp;Bank.
          </div>
        </div>
        <div class="rcol">
          <div class="box">
            <div class="bh">Skills</div>
            <div class="bb">
              Microsoft Tools &bull; Python &bull; JavaScript &bull; HTML &bull;
              Vercel &bull; GitHub &bull; Supabase &bull; Writing &bull;
              Translation &bull; Teaching &bull; Marketing &bull; Accounting
            </div>
          </div>
          <div class="box" style="margin-top:4px;">
            <div class="bh">Languages</div>
            <div class="bb">
              <b>Dutch</b> &mdash; Native<br>
              <b>English</b> &mdash; C2<br>
              <b>Japanese</b> &mdash; A2
            </div>
          </div>
          <div class="box" style="margin-top:4px;">
            <div class="bh">Interests</div>
            <div class="bb">
              Surfing &bull; Marathon (GAME) &bull; History &bull;
              UI/UX &bull; Pok&eacute;mon &bull; Wine
            </div>
          </div>
        </div>
      </div>

      <!-- ROW 3: Work Experience (full width) -->
      <div class="box">
        <div class="bh">Work Experience</div>
        <div class="bb wexp">
          <div class="wrow">
            <div class="wleft">
              <b>Innodata</b><br>
              Outreach Consultant<br>
              Remote &nbsp;|&nbsp; 2026
            </div>
            <div class="wright">
              Driving strategic partnerships across university career centres and academic faculty
              in Japan to build a high-calibre talent pipeline for AI model evaluation and RLHF.
              Managing the entire contributor lifecycle; hosting technical info sessions to
              refining the onboarding of student researchers and subject matter experts.
            </div>
          </div>
          <div class="wdiv"></div>
          <div class="wrow">
            <div class="wleft">
              <b>One Coin English</b><br>
              ESL Teacher<br>
              Japan, Tokyo &nbsp;|&nbsp; 2025
            </div>
            <div class="wright">
              Taught private and group-based conversational English classes to Japanese
              professionals at beginner, intermediate and advanced levels. Provided trial
              lessons that resulted in strong conversion rates related to long-term enrolment.
            </div>
          </div>
          <div class="wdiv"></div>
          <div class="wrow">
            <div class="wleft">
              <b>Stichting Onderwijsconsulenten</b><br>
              Legislative Assistant<br>
              Netherlands, The Hague &nbsp;|&nbsp; 2023
            </div>
            <div class="wright">
              Contributed to the development of operational processes designed to enhance
              equitable access to education for neurodiverse students. Assisted in drafting
              and editing external policy documents. Managed financial administrative
              processes to ensure fiscal compliance.
            </div>
          </div>
          <div class="wdiv"></div>
          <div class="wrow">
            <div class="wleft">
              <b>ASN Bank</b><br>
              Communications Intern<br>
              Netherlands, The Hague &nbsp;|&nbsp; 2022
            </div>
            <div class="wright">
              Communications internship at the Dutch sustainable financial institution ASN Bank.
              Supported internal and external communications, content drafting, and editorial tasks.
            </div>
          </div>
        </div>
      </div>

    </div>
    <div class="statusbar">
      <div class="sp">Done</div>
      <div class="sp" style="flex:1;">&nbsp;</div>
      <div class="sp">Internet zone</div>
    </div>
  </div>
  </div><!-- /relative wrapper -->
</div>

<div class="taskbar">
  <div class="start"><b>Start</b></div>
  <div class="tb-div"></div>
  <div class="tb-win">Fabienne Bruggeman - CV.htm</div>
  <div class="tb-tray">NOW_PLACEHOLDER</div>
</div>

<script>
// ── Context menu ──────────────────────────────────────────────
function showCtxMenu(e) {
  e.preventDefault();
  e.stopPropagation();
  var m = document.getElementById('ctxMenu');
  m.style.display = 'block';
  var x = e.clientX, y = e.clientY;
  if (x + 160 > window.innerWidth) x = window.innerWidth - 160;
  if (y + 140 > window.innerHeight) y = window.innerHeight - 140;
  m.style.left = x + 'px';
  m.style.top  = y + 'px';
}
function hideCtxMenu() {
  var m = document.getElementById('ctxMenu');
  if (m) m.style.display = 'none';
}
// Close menu on any click outside it
document.addEventListener('mousedown', function(e) {
  var m = document.getElementById('ctxMenu');
  if (m && m.style.display === 'block' && !m.contains(e.target)) {
    hideCtxMenu();
  }
});

// ── Desktop icon ──────────────────────────────────────────────
function selectIcon(el) {
  document.querySelectorAll('.deskicon').forEach(function(d){ d.classList.remove('selected'); });
  el.classList.add('selected');
}

// ── Portfolio window ──────────────────────────────────────────
function openPortfolio() {
  var w = document.getElementById('portWin');
  if (w) w.style.display = 'block';
}
function closePortfolio() {
  var w = document.getElementById('portWin');
  if (w) w.style.display = 'none';
}

// ── Tab switching ─────────────────────────────────────────────
function switchTab(name) {
  // tabs
  document.getElementById('tab-writing').classList.remove('active');
  document.getElementById('tab-developing').classList.remove('active');
  document.getElementById('tab-' + name).classList.add('active');
  // panels
  document.getElementById('panel-writing').style.display   = name === 'writing'    ? '' : 'none';
  document.getElementById('panel-developing').style.display = name === 'developing' ? '' : 'none';
}

document.documentElement.style.overflow = 'hidden';
document.body.style.overflow = 'hidden';
</script>
</body>
</html>"""

# Safe injection — no f-string issues
HTML = HTML.replace("BG_CSS_PLACEHOLDER", bg_css)
HTML = HTML.replace("PHOTO_SRC_PLACEHOLDER", photo_src)
HTML = HTML.replace("FOLDER_SRC_PLACEHOLDER", folder_src)
HTML = HTML.replace("NOW_PLACEHOLDER", now)

components.html(HTML, height=5000, scrolling=False)
