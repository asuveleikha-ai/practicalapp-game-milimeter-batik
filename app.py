# app.py - Streamlit Demo - Pabrik Batik Autonomous - Owner Only
# Cara jalanin: streamlit run app.py
# Market: Owner Bisnis Pabrik Batik / Konglomerat Batik / Sritex SAJA - NO PUBLIC MARKET
import streamlit as st

st.set_page_config(page_title="Pabrik Batik Autonomous - Owner Only", layout="wide")
st.markdown("## 🏭 PABRIK BATIK AUTONOMOUS — Game Milimeter Blok 20x100m")
st.markdown("**OWNER ONLY — Khusus Owner Bisnis Pabrik Batik / Konglomerat Batik / Sritex** | NO Retail | NO Pasar Umum")

# --- OWNER GATE ---
if "owner" not in st.session_state:
    st.session_state.owner = False
if not st.session_state.owner:
    st.warning("🔒 Verifikasi Owner dulu sebelum demo.")
    nama = st.text_input("Nama Pabrik / Grup", placeholder="Contoh: Pabrik Batik X / Sritex Group")
    cek = st.checkbox("Saya Owner Pabrik Batik / Konglomerat Batik / Sritex")
    if st.button("BUKA DEMO OWNER →"):
        if cek:
            st.session_state.owner = True
            st.session_state.nama = nama or "Owner Pabrik Batik"
            st.rerun()
        else:
            st.error("Centang dulu verifikasi owner.")
    st.stop()

st.success(f"Selamat datang Owner: {st.session_state.get('nama','-')} | Lahan 20x100m = 2000m² | Hero: Turbin DC 1.5 kW")
tab1, tab2, tab3 = st.tabs(["GAME 1: PABRIK AUTONOMOUS", "GAME 2: SUPER SECURE + INFRARED", "GAME 3: SAAS SCM OWNER"])

with tab1:
    st.subheader("Kayu → Tungku Raksasa → Kettel 500L → Turbin → DC 1.5 kW → Lilin <100°C → Mori")
    if "heat" not in st.session_state:
        st.session_state.heat=20; st.session_state.press=0.0; st.session_state.dc=0.0; st.session_state.kain=0; st.session_state.safety=100
    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("🪵 Masukkan Kayu"): st.session_state.heat=min(220,st.session_state.heat+25); st.session_state.press=min(6,st.session_state.press+0.6)
        if st.button("♻️ Sirkulasi Uap (Pipa 2-3cm)"): st.session_state.press=min(6,st.session_state.press+0.8)
    with c2:
        if st.button("⚡ Nyalakan Turbin DC"): st.session_state.dc=min(1.5, st.session_state.press*0.35)
        if st.button("📯 RELEASE Pluit Safety"): st.session_state.press=max(0,st.session_state.press-2); st.session_state.dc=max(0,st.session_state.dc-0.3)
    with c3:
        lilin = st.slider("Suhu Lilin Parafin + Siongka (°C) — Target 90-95, JANGAN >100", 30, 120, 90)
        if st.button("👕 Produksi Batik Mori"):
            if st.session_state.dc<0.5: st.error("DC kurang, nyalakan turbin dulu.")
            elif lilin<85 or lilin>=100: st.error(f"Suhu lilin harus 90-95°C! Sekarang {lilin}°C"); st.session_state.safety=max(0,st.session_state.safety-10)
            else: st.session_state.kain+=1; st.success("Batik Mori jadi! Lilin meresap sempurna ke pori Mori.")
    st.progress(min(st.session_state.press/6,1.0), text=f"Tekanan: {st.session_state.press:.1f} bar | Panas: {st.session_state.heat}°C")
    st.progress(min(st.session_state.dc/1.5,1.0), text=f"Listrik DC: {st.session_state.dc:.2f} / 1.5 kW")
    st.metric("Kain Jadi", f"{st.session_state.kain} pcs"); st.metric("Safety Score", f"{st.session_state.safety}")
    if st.session_state.press>5: st.warning("⚠️ TEKANAN BERLEBIH! Klik RELEASE Pluit!")
    if st.button("♻️ Jalankan IPAL 3 Bak → Pemda"): st.info("IPAL: Grease Trap → Netralisasi pH 2x2x1.5m → Filtrasi Multi-Layer 10x8x3m → Bak Air Bersih → Pipa IPAL Pemda. Aman.")
    st.caption("Catatan safety: Boiler uap bertekanan wajib dicek teknisi bersertifikat. Ini simulasi logika, bukan tutorial rakit boiler.")

with tab2:
    st.subheader("Super Secure + Super Infrared — 95% / 90%")
    mcb = st.selectbox("Pilih MCB untuk Heavy Industry", ["—", "14A / 1mm² (SALAH)", "50A / 10mm² (BENAR)", "21A / 2.5mm² (SALAH)"])
    if "50A" in mcb: st.success("MCB benar! Kunci terbuka, bisa scan.")
    if st.button("📡 Scan Infrared — Cari Titik Panas"):
        st.info("Titik panas ketemu: Tungku Raksasa → Kettel → Turbin DC 1.5kW → Kompor Lilin → Sensor IMX219")
    st.table({"Beban": ["AC Board","House","Company","Heavy Industry"], "MCB": ["14A","21A","34A","50A"], "Kabel": ["1mm²","2.5mm²","6mm²","10mm²"]})

with tab3:
    st.subheader("SAAS SCM V4.6 ACTIVE — Gudang Besar 22M 20x110=2200m² Gate 6M 7+6+7 GSB 10M | Gudang Kecil C12")
    bahan = st.text_input("Nama Bahan", "Mori Primis")
    if "stok" not in st.session_state: st.session_state.stok=0; st.session_state.cmt=0; st.session_state.profit=0
    if st.button("+ INPUT BARANG MASUK"): st.session_state.stok+=1; st.success(f"INPUT ACTIVE: {bahan} masuk Gudang Besar 22M")
    if st.button("Kirim ke CMT — Owner Only"):
        if st.session_state.stok>0: st.session_state.stok-=1; st.session_state.cmt+=1; st.session_state.profit+=250000
        else: st.error("Stok kosong.")
    st.metric("Stok", st.session_state.stok); st.metric("Order CMT", st.session_state.cmt); st.metric("Profit Owner", f"Rp {st.session_state.profit:,}")
    st.caption("Market: Owner Pabrik Batik / Konglomerat Batik / Sritex SAJA. Tidak ada pasar umum.")
