import base64
import hashlib
import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. PENGATURAN HALAMAN & KOMPONEN
# ==========================================
st.set_page_config(page_title="Dashboard Penjualan", layout="wide")

FOLDER = Path(__file__).parent
FOLDER_KOMPONEN = FOLDER / "microslats_component" / "build"

# Jalur folder proyek tim
KANDIDAT_DATA = [
    "data/clean/indonesia_ecommerce_sales_clean.csv",
    "data/preparation/indonesia_ecommerce_sales_selesai.csv",
    "data/raw/indonesia_ecommerce_sales_challenging.csv",
    "data/processed/clean_indonesia_ecommerce.csv",
    "clean_indonesia_ecommerce.csv",
    "dataset_bersih.csv",
]
FILE_BG = FOLDER / "assets" / "image.png"
FILE_IMAGE2 = FOLDER / "assets" / "image2.png"  # Gambar background sidebar
AKSEN = "#F59E0B"   # Warna aksen
TEKS = "#E5E7EB"

BULAN = ["", "Januari", "Februari", "Maret", "April", "Mei", "Juni",
         "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

LANGKAH = [
    {"judul": "Pilih tanggal",
     "isi": "Klik kotak <b>Tanggal</b> ini, lalu pilih tanggal awal dan akhir. "
            "Semua angka dan grafik ikut berubah.",
     "sel": '[data-testid="stSidebar"] [data-testid="stDateInput"]'},
    {"judul": "Saring data",
     "isi": "Klik di sini untuk memilih <b>kategori produk</b>. Di bawahnya ada filter "
            "<b>provinsi</b> dan <b>cara bayar</b>. Kalau kosong, semua data tampil.",
     "sel": '[data-testid="stSidebar"] [data-testid="stMultiSelect"]'},
    {"judul": "Baca angka utama",
     "isi": "Empat kartu ini berisi pendapatan, jumlah pesanan, "
            "rata-rata per pesanan, dan barang terjual.",
     "sel": ".kartu", "closest": '[data-testid="stHorizontalBlock"]'},
    {"judul": "Ganti jenis tren",
     "isi": "Klik <b>Harian / Mingguan / Bulanan</b> untuk mengubah grafik pendapatan.",
     "sel": '[data-testid="stMainBlock"] [data-testid="stRadio"]', "tab": "Ringkasan"},
    {"judul": "Pindah halaman",
     "isi": "Klik tab ini untuk pindah. <b>Produk</b> berisi produk dan cara bayar terlaris, "
            "<b>Wilayah</b> berisi provinsi dan kota terbanyak.",
     "sel": '[data-baseweb="tab-list"]'},
    {"judul": "Cari dan download",
     "isi": "Di tab <b>Data</b>, ketik ID pesanan untuk mencari, atau klik "
            "<b>Download data</b> untuk menyimpan hasilnya ke CSV.",
     "sel": '[data-testid="stTextInput"]', "tab": "Data"},
]

# ---------- JAVASCRIPT PANDUAN ----------
TUR_JS = r"""
(function () {
  var STEPS = __STEPS__;
  var AKSEN = "__AKSEN__";
  var VERSI = "__VERSI__";
  var PEMICU = __PEMICU__;
  var D = document;

  function definisi(prevPemicu, lama) {
    if (lama) {
      if (lama.tutup) lama.tutup();
      if (lama.onPosisi) {
        window.removeEventListener("scroll", lama.onPosisi, true);
        window.removeEventListener("resize", lama.onPosisi);
      }
      var cssLama = D.getElementById("tur-style");
      if (cssLama) cssLama.remove();
    }

    var T = window.__tur = { versi: VERSI, i: 0, aktif: false, pemicu: prevPemicu,
                             root: null, pop: null, sorot: null, el: null };

    var css =
      "#tur-root .tur-sorot{position:fixed;z-index:999997;border:2px solid " + AKSEN + ";border-radius:10px;" +
      "pointer-events:none;box-shadow:0 0 0 9999px rgba(0,0,0,.45),0 0 18px " + AKSEN + "88;transition:all .25s ease;}" +
      "#tur-root .tur-pop{position:fixed;z-index:999998;width:300px;max-width:calc(100vw - 24px);" +
      "background:#0F172A;color:#E5E7EB;border:2px solid " + AKSEN + ";border-radius:12px;padding:14px 16px;" +
      "box-shadow:0 10px 34px rgba(0,0,0,.6);font-family:Inter,-apple-system,BlinkMacSystemFont,sans-serif;" +
      "font-size:14px;line-height:1.5;transition:left .25s ease,top .25s ease;}" +
      "#tur-root .tur-info{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:#9CA3AF;margin-bottom:4px;}" +
      "#tur-root .tur-x{background:none;border:none;color:#9CA3AF;cursor:pointer;font-size:20px;line-height:1;padding:0;}" +
      "#tur-root .tur-judul{font-weight:700;color:#fff;font-size:16px;margin-bottom:4px;}" +
      "#tur-root .tur-isi b{color:#fff;}" +
      "#tur-root .tur-tombol{display:flex;gap:8px;margin-top:12px;}" +
      "#tur-root .tur-tombol button{flex:1;padding:7px 0;border-radius:8px;border:1px solid rgba(255,255,255,.2);" +
      "background:transparent;color:#E5E7EB;cursor:pointer;font-size:13px;}" +
      "#tur-root .tur-tombol button.utama{background:" + AKSEN + ";color:#111;border-color:" + AKSEN + ";font-weight:600;}" +
      "#tur-root .tur-tombol button:disabled{opacity:.35;cursor:default;}" +
      "#tur-root .tur-panah{position:absolute;width:16px;height:16px;background:#0F172A;transform:rotate(45deg);}" +
      "#tur-root .tur-panah.p-kiri{left:-9px;border-left:2px solid " + AKSEN + ";border-bottom:2px solid " + AKSEN + ";animation:tkiri 1s ease-in-out infinite;}" +
      "#tur-root .tur-panah.p-atas{top:-9px;border-top:2px solid " + AKSEN + ";border-left:2px solid " + AKSEN + ";animation:tatas 1s ease-in-out infinite;}" +
      "#tur-root .tur-panah.p-bawah{bottom:-9px;border-bottom:2px solid " + AKSEN + ";border-right:2px solid " + AKSEN + ";animation:tbawah 1s ease-in-out infinite;}" +
      "@keyframes tkiri{0%,100%{margin-left:0}50%{margin-left:-5px}}" +
      "@keyframes tatas{0%,100%{margin-top:0}50%{margin-top:-5px}}" +
      "@keyframes tbawah{0%,100%{margin-bottom:0}50%{margin-bottom:-5px}}";
    var st = D.createElement("style");
    st.id = "tur-style";
    st.textContent = css;
    D.head.appendChild(st);

    function buatRoot() {
      T.root = D.createElement("div");
      T.root.id = "tur-root";
      T.sorot = D.createElement("div");
      T.sorot.className = "tur-sorot";
      T.pop = D.createElement("div");
      T.pop.className = "tur-pop";
      T.root.appendChild(T.sorot);
      T.root.appendChild(T.pop);
      D.body.appendChild(T.root);
    }

    T.tutup = function () {
      T.aktif = false;
      if (T.root) { T.root.remove(); T.root = null; }
    };

    function klikTab(nama) {
      var tabs = D.querySelectorAll('button[role="tab"]');
      for (var k = 0; k < tabs.length; k++) {
        if (tabs[k].textContent.trim() === nama) { tabs[k].click(); return; }
      }
    }

    function cari(s) {
      var el = D.querySelector(s.sel);
      if (el && s.closest) el = el.closest(s.closest);
      return el;
    }

    function render(s, i) {
      var n = STEPS.length;
      T.pop.innerHTML =
        '<div class="tur-panah"></div>' +
        '<div class="tur-info"><span>Langkah ' + (i + 1) + ' dari ' + n + '</span>' +
        '<button class="tur-x" title="Tutup">&times;</button></div>' +
        '<div class="tur-judul">' + s.judul + '</div>' +
        '<div class="tur-isi">' + s.isi + '</div>' +
        '<div class="tur-tombol">' +
        '<button class="mundur"' + (i === 0 ? ' disabled' : '') + '>Kembali</button>' +
        '<button class="utama maju">' + (i === n - 1 ? 'Selesai' : 'Lanjut') + '</button></div>';
      T.pop.querySelector(".tur-x").onclick = T.tutup;
      T.pop.querySelector(".mundur").onclick = function () { tampil(T.i - 1); };
      T.pop.querySelector(".maju").onclick = function () {
        if (T.i >= n - 1) T.tutup(); else tampil(T.i + 1);
      };
    }

    function posisi() {
      if (!T.aktif || !T.root) return;
      var pop = T.pop, sorot = T.sorot;
      var W = window.innerWidth, H = window.innerHeight;
      var pw = pop.offsetWidth, ph = pop.offsetHeight;
      var panah = pop.querySelector(".tur-panah");
      if ((!T.el || !T.el.isConnected) && STEPS[T.i]) T.el = cari(STEPS[T.i]);
      var r = T.el ? T.el.getBoundingClientRect() : null;

      if (!r || (r.width === 0 && r.height === 0)) {
        sorot.style.display = "none";
        panah.style.display = "none";
        pop.style.left = (W - pw - 24) + "px";
        pop.style.top = (H - ph - 24) + "px";
        return;
      }

      sorot.style.display = "block";
      sorot.style.left = (r.left - 6) + "px";
      sorot.style.top = (r.top - 6) + "px";
      sorot.style.width = (r.width + 12) + "px";
      sorot.style.height = (r.height + 12) + "px";

      var gap = 24, left, top, arah = null;
      var cx = r.left + r.width / 2, cy = r.top + r.height / 2;

      if (r.left < W * 0.4 && r.right + gap + pw + 12 < W) {
        arah = "kiri"; left = r.right + gap; top = cy - ph / 2;
      } else if (r.bottom + gap + ph + 12 < H) {
        arah = "atas"; left = cx - pw / 2; top = r.bottom + gap;
      } else if (r.top - gap - ph - 12 > 0) {
        arah = "bawah"; left = cx - pw / 2; top = r.top - gap - ph;
      } else {
        left = (W - pw) / 2; top = H - ph - 24;
      }

      left = Math.max(12, Math.min(W - pw - 12, left));
      top = Math.max(12, Math.min(H - ph - 12, top));
      pop.style.left = left + "px";
      pop.style.top = top + "px";

      if (!arah) { panah.style.display = "none"; return; }
      panah.style.display = "block";
      panah.className = "tur-panah p-" + arah;
      if (arah === "kiri") {
        panah.style.left = ""; panah.style.top = Math.max(16, Math.min(ph - 32, cy - top - 8)) + "px";
      } else {
        panah.style.top = ""; panah.style.left = Math.max(16, Math.min(pw - 32, cx - left - 8)) + "px";
      }
    }

    function cariTunggu(i, n) {
      if (!T.aktif || T.i !== i) return;
      var el = cari(STEPS[i]);
      var r = el ? el.getBoundingClientRect() : null;
      if ((!r || (r.width === 0 && r.height === 0)) && n > 0) {
        setTimeout(function () { cariTunggu(i, n - 1); }, 150);
        return;
      }
      T.el = el;
      if (el) el.scrollIntoView({ block: "center", behavior: "smooth" });
      posisi();
      setTimeout(posisi, 400);
      setTimeout(posisi, 800);
    }

    function tampil(i) {
      T.i = i;
      T.aktif = true;
      var s = STEPS[i];
      if (!T.root) buatRoot();
      T.el = null;
      render(s, i);
      posisi();
      if (s.tab) klikTab(s.tab);
      cariTunggu(i, 14);
    }

    T.onPosisi = posisi;
    window.addEventListener("scroll", posisi, true);
    window.addEventListener("resize", posisi);

    T.cek = function (p) {
      var pertama = (T.pemicu === -1);
      if (p === T.pemicu) return;
      T.pemicu = p;
      if (pertama) {
        if (p === 0) setTimeout(function () { tampil(0); }, 3300);
      } else {
        tampil(0);
      }
    };
  }

  var lama = window.__tur;
  if (!lama || lama.versi !== VERSI) {
    definisi(lama ? lama.pemicu : -1, lama);
  }
  window.__tur.cek(PEMICU);
})();
"""

CSS_INTRO = """
#intro-screen {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    background-color: #090D16 !important;
    z-index: 9999999 !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    animation: slideOutLeft 1.5s cubic-bezier(0.77, 0, 0.175, 1) 2.0s forwards;
}
#intro-screen h1 {
    color: #FFFFFF !important; font-size: 2.8rem !important; font-weight: 700;
    letter-spacing: 2px; margin: 0; animation: slideUp 0.8s ease-out;
}
#intro-screen p {
    color: #94A3B8 !important; font-size: 1rem; margin-top: 8px;
    letter-spacing: 0.05em; animation: fadeIn 1.2s ease-out;
}
#intro-screen .made-by {
    color: #64748B !important; font-size: 0.85rem; font-weight: 500;
    margin-top: 30px; letter-spacing: 1.5px; animation: fadeIn 1.6s ease-out;
    font-family: 'Courier New', Monospace, monospace;
}

.tech-kou {
    color: #F59E0B !important;
    font-weight: 700;
    letter-spacing: 3px;
    text-shadow: 0 0 8px rgba(245, 158, 11, 0.8), 0 0 15px rgba(245, 158, 11, 0.4);
    display: inline-block;
    animation: techFlicker 2s infinite alternate;
}

@keyframes techFlicker {
    0%, 100% { opacity: 1; text-shadow: 0 0 8px rgba(245, 158, 11, 0.8), 0 0 15px rgba(245, 158, 11, 0.4); }
    50% { opacity: 0.8; text-shadow: 0 0 3px rgba(245, 158, 11, 0.5); }
    80% { opacity: 1; text-shadow: 0 0 12px rgba(245, 158, 11, 1), 0 0 20px rgba(245, 158, 11, 0.6); }
}

@keyframes slideOutLeft {
    0% { transform: translateX(0); opacity: 1; }
    100% { transform: translateX(-100%); opacity: 1; visibility: hidden; z-index: -1; }
}

@keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
"""


# ---------- FUNGSIONALITAS ANIMASI "MACHINE LEARNING" (ASAP DIKECILKAN) ----------
def render_tech_text(text="Machine\nLearning", height=110):
    lines = text.split("\n")
    safe_lines = json.dumps(lines, ensure_ascii=True).replace("<", "\\u003c")
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 100%; height: 100%; overflow: hidden; background: transparent; }
      #tech-container { width: 100%; height: __HEIGHT__px; position: relative; }
      canvas { display: block; width: 100%; height: 100%; touch-action: pan-y; }
    </style>
    </head>
    <body>
      <div id="tech-container"><canvas id="tech-canvas" role="img"></canvas></div>
      <script>
        const canvas = document.getElementById('tech-canvas');
        const ctx = canvas.getContext('2d');
        const lines = __LINES__;
        const container = document.getElementById('tech-container');
        let width = 1, height = 1, dpr = 1, glyphs = [];
        let hoverIndex = -1, frame = 0;
        const started = performance.now();
        let kicks = [];

        function resize() {
          const bounds = container.getBoundingClientRect();
          width = Math.max(1, bounds.width);
          height = Math.max(1, bounds.height);
          dpr = Math.min(window.devicePixelRatio || 1, 2);
          canvas.width = Math.round(width * dpr);
          canvas.height = Math.round(height * dpr);
          ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

          const fontSize = Math.max(16, Math.min(30, width * 0.10));
          ctx.font = `700 ${fontSize}px Inter, Arial, sans-serif`;

          glyphs = [];
          kicks = [];
          const lineHeight = fontSize * 1.3;
          const totalH = lines.length * lineHeight;
          let startY = (height - totalH) / 2 + fontSize * 0.85;

          lines.forEach((lineText, lineIdx) => {
            const widths = Array.from(lineText, char => ctx.measureText(char).width);
            const totalW = widths.reduce((a, b) => a + b, 0);
            let x = (width - totalW) / 2;

            Array.from(lineText).forEach((char, charIdx) => {
              glyphs.push({
                char, x, y: startY + lineIdx * lineHeight,
                width: widths[charIdx], size: fontSize,
                line: lineIdx
              });
              kicks.push(0);
              x += widths[charIdx];
            });
          });
        }

        function closestGlyph(x, y) {
          if (!glyphs.length) return -1;
          let best = -1, distance = Infinity;
          glyphs.forEach((glyph, index) => {
            const cx = glyph.x + glyph.width / 2;
            const cy = glyph.y - glyph.size / 2;
            const dist = Math.hypot(x - cx, y - cy);
            if (dist < distance) { distance = dist; best = index; }
          });
          return distance < glyphs[0].size * 1.2 ? best : -1;
        }

        function drawFrame(glyph, index, now) {
          // Efek asap/kotak diperkecil agar lebih elegan
          const padX = Math.max(2, glyph.size * 0.05), padY = Math.max(2, glyph.size * 0.05);
          const x = glyph.x - padX, y = glyph.y - glyph.size * 0.82 - padY;
          const w = glyph.width + padX * 2, h = glyph.size * 0.95 + padY * 2;
          
          ctx.save();
          ctx.strokeStyle = 'rgba(245, 158, 11, 0.8)';
          ctx.lineWidth = 0.8;
          ctx.setLineDash([2, 2]);
          ctx.lineDashOffset = -now * 0.02;
          ctx.shadowColor = '#F59E0B';
          ctx.shadowBlur = 4;
          ctx.strokeRect(x, y, w, h);
          ctx.setLineDash([]);
          ctx.shadowBlur = 0;
          ctx.fillStyle = 'rgba(245, 158, 11, 0.85)';
          ctx.font = '600 7px ui-monospace, monospace';
          ctx.fillText(`${glyph.char}`, x, Math.max(6, y - 2));

          for (let i = 0; i < 5; i++) {
            const seed = (index + 1) * 97 + i * 31;
            const phase = now * (0.001 + (i % 4) * 0.0002) + seed;
            const side = i % 4;
            const t = (Math.sin(phase) + 1) / 2;
            const sx = side === 0 ? x + t * w : side === 1 ? x + w : side === 2 ? x + (1 - t) * w : x;
            const sy = side === 0 ? y : side === 1 ? y + t * h : side === 2 ? y + h : y + (1 - t) * h;
            const distance = 2 + (i % 2) * 2;
            const px = sx + (side === 1 ? distance : side === 3 ? -distance : 0);
            const py = sy + (side === 0 ? -distance : side === 2 ? distance : 0);
            ctx.globalAlpha = 0.3 + (Math.sin(phase * 2) + 1) * 0.2;
            ctx.fillRect(Math.round(px), Math.round(py), 1.5, 1.5);
          }
          ctx.restore();
        }

        function draw(now) {
          ctx.clearRect(0, 0, width, height);
          const active = hoverIndex;

          glyphs.forEach((glyph, index) => {
            const kickElapsed = kicks[index] ? (now - kicks[index]) / 1000 : 1;
            const kickOffset = kickElapsed < 0.55 ? -Math.sin(Math.PI * kickElapsed / 0.55) * glyph.size * 0.25 : 0;
            ctx.save();
            ctx.font = `700 ${glyph.size}px Inter, Arial, sans-serif`;
            ctx.shadowColor = 'rgba(245, 158, 11, 0.7)';
            ctx.shadowBlur = index === active ? 10 : 4;
            ctx.fillStyle = index === active ? '#FFD27A' : '#F59E0B';
            ctx.fillText(glyph.char, glyph.x, glyph.y + kickOffset);

            if (index === active) {
              ctx.lineWidth = 1;
              ctx.strokeStyle = '#FFD27A';
              ctx.setLineDash([2, 2]);
              ctx.strokeText(glyph.char, glyph.x, glyph.y + kickOffset);
            }
            ctx.restore();
          });

          if (active >= 0 && glyphs[active]) drawFrame(glyphs[active], active, now);
          frame = requestAnimationFrame(draw);
        }

        canvas.addEventListener('pointermove', event => {
          const bounds = canvas.getBoundingClientRect();
          hoverIndex = closestGlyph(event.clientX - bounds.left, event.clientY - bounds.top);
          canvas.style.cursor = hoverIndex >= 0 ? 'pointer' : 'default';
        });
        canvas.addEventListener('pointerleave', () => { hoverIndex = -1; });
        canvas.addEventListener('pointerdown', event => {
          const bounds = canvas.getBoundingClientRect();
          const idx = closestGlyph(event.clientX - bounds.left, event.clientY - bounds.top);
          if (idx >= 0) kicks[idx] = performance.now();
        });

        const observer = new ResizeObserver(resize);
        observer.observe(container);
        resize();
        draw(started);
      </script>
    </body>
    </html>
    """.replace("__HEIGHT__", str(max(1, int(height)))).replace("__LINES__", safe_lines)
    components.html(html_code, height=height)


def baca_gambar(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None


def rupiah(x):
    return "Rp " + f"{x:,.0f}".replace(",", ".")


def angka(x):
    return f"{x:,.0f}".replace(",", ".")


# --- BACA GAMBAR BACKGROUND ---
img = baca_gambar(FILE_BG)
if img:
    bg_normal = (f'background: linear-gradient(rgba(10,14,23,0.90), rgba(15,23,42,0.94)), '
                 f'url("data:image/png;base64,{img}"); '
                 f'background-size: cover; background-position: center; background-attachment: fixed;')
else:
    bg_normal = "background: linear-gradient(135deg, #0A0E17 0%, #0F172A 100%);"

img_sidebar = baca_gambar(FILE_IMAGE2)
if img_sidebar:
    bg_sidebar = (f'background: linear-gradient(rgba(15, 23, 42, 0.82), rgba(15, 23, 42, 0.90)), '
                  f'url("data:image/png;base64,{img_sidebar}"); '
                  f'background-size: cover; background-position: center;')
else:
    bg_sidebar = "background-color: rgba(15, 23, 42, 0.95);"


# ==========================================
# 2. FITUR MODE TAMPILAN (NORMAL / CIHUY)
# ==========================================
st.sidebar.header("Mode Tampilan")
mode_tampilan = st.sidebar.radio("Pilih Mode:", ["Mode Normal", "Mode Cihuy"], index=0)

# Panggil komponen murni tanpa parameter key
if FOLDER_KOMPONEN.exists():
    microslats = components.declare_component("microslats", path=str(FOLDER_KOMPONEN))
    microslats()

if mode_tampilan == "Mode Cihuy":
    # Mode Cihuy: Background transparan + Iframe WebGL dipaksa aktif & Teks berdampingan shadow
    bg_app = "background: transparent !important; background-color: transparent !important;"
    css_iframe = """
    iframe[data-testid="stCustomComponentV1"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: -1 !important;
        pointer-events: none !important;
        border: none !important;
        display: block !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    /* Efek Kontras & Outline Hitam Elegan untuk Teks di Mode Cihuy */
    h1, h2, h3, h4, p, label, span, .stCaption {
        text-shadow: 0px 2px 6px #000000, 0px 0px 10px #000000 !important;
    }
    .kartu {
        background: rgba(10, 14, 23, 0.85) !important;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(0, 240, 255, 0.25) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6);
    }
    .ringkasan {
        background: rgba(10, 14, 23, 0.88) !important;
        backdrop-filter: blur(8px);
        border-left: 3px solid #00F0FF !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6);
    }
    """
else:
    # Mode Normal: Sembunyikan iframe WebGL murni via CSS
    bg_app = bg_normal
    css_iframe = """
    iframe[data-testid="stCustomComponentV1"] {
        display: none !important;
    }
    """

st.markdown(f"""
<style>
{CSS_INTRO}

.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
    {bg_app}
    color: {TEKS};
}}

{css_iframe}

h1, h2, h3, h4, p, label, span {{ color: {TEKS}; }}

[data-testid="stSidebar"] {{
    {bg_sidebar}
    border-right: 1px solid rgba(255,255,255,0.08);
}}

[data-baseweb="tag"] {{
    background-color: rgba(245,158,11,0.15) !important;
    border: 1px solid rgba(245,158,11,0.5) !important;
}}
[data-baseweb="tag"] * {{ color: {TEKS} !important; }}

.stTabs [aria-selected="true"] {{ color: {AKSEN} !important; }}
.stTabs [data-baseweb="tab-highlight"] {{ background-color: {AKSEN} !important; }}

.kartu {{
    background: rgba(30,41,59,0.55);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 1rem 1.2rem;
}}
.kartu .judul {{ color: #9CA3AF; font-size: 0.8rem; margin-bottom: 4px; }}
.kartu .isi {{ color: #FFFFFF; font-size: 1.4rem; font-weight: 700; white-space: nowrap; }}

.ringkasan {{
    background: rgba(30,41,59,0.55);
    border-left: 3px solid {AKSEN};
    border-radius: 6px;
    padding: 0.9rem 1.2rem;
    line-height: 1.7;
    color: {TEKS};
}}
</style>
""", unsafe_allow_html=True)

# Intro Screen
if "intro_tampil" not in st.session_state:
    st.session_state.intro_tampil = True
    st.markdown("""
    <div id="intro-screen">
        <h1>Dashboard Analytics</h1>
        <p>Indonesia E-Commerce Executive Report</p>
        <div class="made-by">made by <span class="tech-kou">MACHINE LEARNING</span></div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# 3. BACA DATA
# ==========================================
@st.cache_data
def muat_data():
    path = next((FOLDER / n for n in KANDIDAT_DATA if (FOLDER / n).exists()), None)
    if path is None:
        raise FileNotFoundError(
            f"Taruh salah satu file ini di folder {FOLDER}: {', '.join(KANDIDAT_DATA)}"
        )
    df = pd.read_csv(path, encoding="utf-8-sig")

    def cari_kolom(kata_kunci, default_nama):
        for col in df.columns:
            if any(k.lower() in col.lower() for k in kata_kunci):
                return col
        return default_nama

    col_tgl = cari_kolom(["order_date", "waktu", "created", "tanggal", "tgl"], "order_date")
    col_bayar = cari_kolom(["total_payment", "total_pembayaran", "total_amount", "harga", "price"], "Total Pembayaran")
    col_kat = cari_kolom(["product_categories", "kategori", "category"], "product_categories")
    col_prov = cari_kolom(["provinsi", "province", "state"], "Provinsi")
    col_metode = cari_kolom(["metode", "payment_method", "pembayaran"], "Metode Pembayaran")
    col_qty = cari_kolom(["total_qty", "quantity", "jumlah", "qty"], "total_qty")
    col_kota = cari_kolom(["kota", "kabupaten", "city"], "Kota/Kabupaten")
    col_ship = cari_kolom(["opsi_pengiriman", "shipping", "kurir"], "Opsi Pengiriman")

    if col_tgl in df.columns:
        df["order_date"] = pd.to_datetime(df[col_tgl], errors="coerce")
    else:
        df["order_date"] = pd.Timestamp.now()
        st.warning(f"Kolom tanggal tidak terdeteksi otomatis. Kolom yang ada di CSV: {list(df.columns)}")

    df["order_date"] = df["order_date"].fillna(pd.Timestamp.now())
    df["jam"] = df["order_date"].dt.hour
    df["hari"] = df["order_date"].dt.dayofweek

    df["Total Pembayaran"] = pd.to_numeric(df[col_bayar], errors="coerce").fillna(0) if col_bayar in df.columns else 0
    df["total_qty"] = pd.to_numeric(df[col_qty], errors="coerce").fillna(1) if col_qty in df.columns else 1
    df["Provinsi"] = df[col_prov] if col_prov in df.columns else "Lainnya"
    df["Metode Pembayaran"] = df[col_metode] if col_metode in df.columns else "Lainnya"
    df["Kota/Kabupaten"] = df[col_kota] if col_kota in df.columns else "Lainnya"
    df["Opsi Pengiriman"] = df[col_ship] if col_ship in df.columns else "Lainnya"

    if col_kat in df.columns:
        df["daftar_kategori"] = df[col_kat].astype(str).fillna("").apply(
            lambda s: [k.strip() for k in s.split(",") if k.strip()]
        )
    else:
        df["daftar_kategori"] = [["Lainnya"]] * len(df)

    return df


try:
    df = muat_data()
except Exception as e:
    st.error(str(e))
    st.stop()


# ==========================================
# 4. FILTER
# ==========================================
st.sidebar.header("Filter")

tgl_min, tgl_max = df["order_date"].min().date(), df["order_date"].max().date()
rentang = st.sidebar.date_input("Tanggal", value=(tgl_min, tgl_max),
                                min_value=tgl_min, max_value=tgl_max)

semua_kategori = sorted({k for lst in df["daftar_kategori"] for k in lst})
pilih_kategori = st.sidebar.multiselect("Kategori produk", semua_kategori,
                                        placeholder="Semua kategori")
pilih_provinsi = st.sidebar.multiselect("Provinsi", sorted(df["Provinsi"].dropna().unique()),
                                        placeholder="Semua provinsi")
pilih_bayar = st.sidebar.multiselect("Metode pembayaran", sorted(df["Metode Pembayaran"].dropna().unique()),
                                     placeholder="Semua metode")

if "pemicu" not in st.session_state:
    st.session_state.pemicu = 0


def buka_panduan():
    st.session_state.pemicu += 1


st.sidebar.markdown("---")
st.sidebar.button("Lihat panduan", on_click=buka_panduan, use_container_width=True)

st.sidebar.markdown("<div style='text-align:center; color:#94A3B8; font-size:11px; letter-spacing:2px; margin-top:20px;'>MADE BY</div>", unsafe_allow_html=True)
with st.sidebar:
    render_tech_text("Machine\nLearning", height=110)

d = df.copy()
if isinstance(rentang, (tuple, list)) and len(rentang) == 2:
    d = d[(d["order_date"].dt.date >= rentang[0]) & (d["order_date"].dt.date <= rentang[1])]
if pilih_kategori:
    d = d[d["daftar_kategori"].apply(lambda lst: any(k in pilih_kategori for k in lst))]
if pilih_provinsi:
    d = d[d["Provinsi"].isin(pilih_provinsi)]
if pilih_bayar:
    d = d[d["Metode Pembayaran"].isin(pilih_bayar)]


# ==========================================
# 5. PANDUAN BERPANAH
# ==========================================
_kode = (TUR_JS.replace("__STEPS__", json.dumps(LANGKAH, ensure_ascii=False))
               .replace("__AKSEN__", AKSEN))
_versi = hashlib.md5(_kode.encode()).hexdigest()[:8]
_kode = _kode.replace("__VERSI__", _versi).replace("__PEMICU__", str(st.session_state.pemicu))

components.html(
    "<script>var kode = " + json.dumps(_kode).replace("</", "<\\/") + ";"
    "var D = window.parent.document;"
    "var s = D.createElement('script'); s.textContent = kode;"
    "D.body.appendChild(s); s.remove();</script>",
    height=0,
)


# ==========================================
# 6. JUDUL + KARTU ANGKA
# ==========================================
st.title("Dashboard Penjualan")
st.caption("Ringkasan pesanan toko online: pendapatan, produk, dan wilayah pembeli.")

if d.empty:
    st.warning("Tidak ada data untuk filter ini. Coba longgarkan filternya.")
    st.stop()

total_pendapatan = d["Total Pembayaran"].sum()
total_pesanan = len(d)
rata_rata = d["Total Pembayaran"].mean()
total_barang = d["total_qty"].sum()

for kolom, judul, isi in zip(
    st.columns(4),
    ["Pendapatan", "Jumlah Pesanan", "Rata-rata per Pesanan", "Barang Terjual"],
    [rupiah(total_pendapatan), angka(total_pesanan), rupiah(rata_rata), angka(total_barang)],
):
    kolom.markdown(f'<div class="kartu"><div class="judul">{judul}</div>'
                   f'<div class="isi">{isi}</div></div>', unsafe_allow_html=True)

bulanan = d.groupby(d["order_date"].dt.to_period("M"))["Total Pembayaran"].sum()
bulan_terbaik = bulanan.idxmax()
kategori_teratas = d.explode("daftar_kategori")["daftar_kategori"].value_counts().index[0]
provinsi_teratas = d["Provinsi"].value_counts().index[0]
bayar_teratas = d["Metode Pembayaran"].value_counts().index[0]
jam_ramai = int(d["jam"].value_counts().index[0])

st.markdown("")
st.markdown(
    f'<div class="ringkasan">'
    f'Bulan terbaik: <b>{BULAN[bulan_terbaik.month]} {bulan_terbaik.year}</b> '
    f'({rupiah(bulanan.max())}).<br>'
    f'Produk paling sering dibeli: <b>{kategori_teratas}</b>. '
    f'Pembeli terbanyak dari <b>{provinsi_teratas.title()}</b>.<br>'
    f'Cara bayar favorit: <b>{bayar_teratas}</b>. '
    f'Jam paling ramai: <b>{jam_ramai:02d}.00</b>.'
    f'</div>', unsafe_allow_html=True
)
st.markdown("")


# ==========================================
# 7. FUNGSI GRAFIK & TAB
# ==========================================
def rapikan(fig, tinggi=360):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=TEKS, size=12),
        margin=dict(l=10, r=10, t=10, b=10), height=tinggi,
        xaxis=dict(gridcolor="rgba(255,255,255,0.07)"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.07)"),
    )
    return fig


def grafik_batang_mendatar(data, x, y, tinggi=360):
    fig = px.bar(data, x=x, y=y, orientation="h", text=x)
    fig.update_traces(marker_color=AKSEN, textposition="outside")
    fig.update_yaxes(categoryorder="total ascending", title="")
    fig.update_xaxes(title="")
    return rapikan(fig, tinggi)


tab1, tab2, tab3, tab4 = st.tabs(["Ringkasan", "Produk", "Wilayah", "Data"])

# ---------- TAB RINGKASAN ----------
with tab1:
    st.subheader("Pendapatan dari waktu ke waktu")
    pilihan = st.radio("Lihat per:", ["Harian", "Mingguan", "Bulanan"],
                       index=2, horizontal=True)
    aturan = {"Harian": "D", "Mingguan": "W", "Bulanan": "MS"}[pilihan]
    tren = d.set_index("order_date")["Total Pembayaran"].resample(aturan).sum().reset_index()
    fig = px.line(tren, x="order_date", y="Total Pembayaran",
                  labels={"order_date": "", "Total Pembayaran": "Pendapatan (Rp)"})
    fig.update_traces(line_color=AKSEN, line_width=2.5)
    st.plotly_chart(rapikan(fig, 340), use_container_width=True)

    kiri, kanan = st.columns(2)
    with kiri:
        st.subheader("Jam paling ramai")
        per_jam = d.groupby("jam").size().reset_index(name="Pesanan")
        fig = px.bar(per_jam, x="jam", y="Pesanan", labels={"jam": "Jam"})
        fig.update_traces(marker_color=AKSEN)
        st.plotly_chart(rapikan(fig, 300), use_container_width=True)
    with kanan:
        st.subheader("Hari paling ramai")
        per_hari = d.groupby("hari").size().reindex(range(7), fill_value=0).reset_index(name="Pesanan")
        per_hari["Hari"] = per_hari["hari"].map(lambda i: HARI[i])
        fig = px.bar(per_hari, x="Hari", y="Pesanan")
        fig.update_traces(marker_color=AKSEN)
        st.plotly_chart(rapikan(fig, 300), use_container_width=True)

# ---------- TAB PRODUK ----------
with tab2:
    kiri, kanan = st.columns(2)
    with kiri:
        st.subheader("10 produk paling sering dibeli")
        kat = d.explode("daftar_kategori")["daftar_kategori"].value_counts().head(10).reset_index()
        kat.columns = ["Kategori", "Pesanan"]
        st.plotly_chart(grafik_batang_mendatar(kat, "Pesanan", "Kategori"), use_container_width=True)
        st.caption("Satu pesanan bisa berisi beberapa kategori, jadi dihitung di tiap kategorinya.")
    with kanan:
        st.subheader("Cara pembayaran")
        bayar = d["Metode Pembayaran"].value_counts().head(8).reset_index()
        bayar.columns = ["Metode", "Pesanan"]
        st.plotly_chart(grafik_batang_mendatar(bayar, "Pesanan", "Metode"), use_container_width=True)

    st.subheader("Jasa pengiriman")
    kirim = d["Opsi Pengiriman"].value_counts().head(8).reset_index()
    kirim.columns = ["Pengiriman", "Pesanan"]
    st.plotly_chart(grafik_batang_mendatar(kirim, "Pesanan", "Pengiriman", 320), use_container_width=True)

# ---------- TAB WILAYAH ----------
with tab3:
    kiri, kanan = st.columns(2)
    with kiri:
        st.subheader("10 provinsi terbanyak")
        prov = d["Provinsi"].str.title().value_counts().head(10).reset_index()
        prov.columns = ["Provinsi", "Pesanan"]
        st.plotly_chart(grafik_batang_mendatar(prov, "Pesanan", "Provinsi"), use_container_width=True)
    with kanan:
        st.subheader("10 kota/kabupaten terbanyak")
        kota = d["Kota/Kabupaten"].str.title().value_counts().head(10).reset_index()
        kota.columns = ["Kota", "Pesanan"]
        st.plotly_chart(grafik_batang_mendatar(kota, "Pesanan", "Kota"), use_container_width=True)

# ---------- TAB DATA ----------
with tab4:
    st.write(f"Menampilkan **{angka(total_pesanan)}** pesanan sesuai filter.")
    
    kiri_data, kanan_data = st.columns([2, 1])
    with kiri_data:
        cari = st.text_input("Cari ID pesanan", placeholder="contoh: ORD_0000010")
    with kanan_data:
        pilih_kurs = st.selectbox("Mata Uang Tampilan:", ["IDR (Rp)", "USD ($)", "EUR (€)"])

    tabel = d.drop(columns=["daftar_kategori", "jam", "hari"], errors="ignore").copy()
    
    if cari and "order_id" in tabel.columns:
        tabel = tabel[tabel["order_id"].astype(str).str.contains(cari, case=False, na=False)]

    kata_kunci_uang = [
        "pembayaran", "price", "harga", "ongkir", "ongkos", "kirim", "biaya", 
        "potongan", "shipping", "cost", "total_amount", "subtotal", "diskon", 
        "discount", "fee", "nilai"
    ]
    
    kolom_uang = [col for col in tabel.columns if any(k in col.lower() for k in kata_kunci_uang)]
    format_uang = "Rp %'d"
    KURS = 1.0

    if pilih_kurs == "USD ($)":
        KURS = 18059
        format_uang = "$ %.2f"
    elif pilih_kurs == "EUR (€)":
        KURS = 20284
        format_uang = "€ %.2f"

    for col in kolom_uang:
        s_clean = tabel[col].astype(str).str.replace(r"[^\d.-]", "", regex=True)
        tabel[col] = pd.to_numeric(s_clean, errors="coerce").fillna(0)
        if KURS != 1.0:
            tabel[col] = tabel[col] / KURS

    konfig_kolom = {
        col: st.column_config.NumberColumn(col, format=format_uang) for col in kolom_uang
    }

    if "total_qty" in tabel.columns:
        tabel["total_qty"] = pd.to_numeric(tabel["total_qty"], errors="coerce").fillna(0)
        konfig_kolom["total_qty"] = st.column_config.NumberColumn("Total Qty", format="%d")
        
    if "total_weight_gr" in tabel.columns:
        tabel["total_weight_gr"] = pd.to_numeric(tabel["total_weight_gr"], errors="coerce").fillna(0)
        konfig_kolom["total_weight_gr"] = st.column_config.NumberColumn("Total Weight (gr)", format="%d")

    st.dataframe(
        tabel,
        column_config=konfig_kolom,
        height=350,
        use_container_width=True
    )
    
    st.download_button(
        "Download data (CSV)",
        tabel.to_csv(index=False).encode("utf-8"),
        file_name="data_penjualan.csv",
        mime="text/csv"
    )