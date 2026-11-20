# app.py - aichaliveret company - aichaliveret by meta.ai
# Practical Application - SaaS System for Market Intelligence & Decision Support
# Bukan permainan. Sistem simulasi observasi untuk pendukung pengambilan keputusan.
# Tidak memberikan instruksi beli/jual. Hanya skenario, tingkat keyakinan, risiko.
import streamlit as st
st.set_page_config(page_title="aichaliveret - Practical Application Pabrik Batik", layout="wide")
st.markdown("## aichaliveret company — aichaliveret by meta.ai")
st.markdown("### Practical Application — SaaS System for Market Intelligence & Decision Support")
st.markdown("**Keputusan yang baik tidak lahir dari kecepatan, melainkan dari kejernihan. Akurasi sebelum kecepatan, tanggung jawab sebelum popularitas.**")
st.markdown("**OWNER ONLY — Owner Bisnis Pabrik Batik / Konglomerat Batik / Sritex** | Lahan 20x100m = 2000m2")
if "owner" not in st.session_state: st.session_state.owner=False
if not st.session_state.owner:
    st.warning("Verifikasi Owner dulu.")
    nama=st.text_input("Nama Pabrik / Grup", placeholder="Contoh: Pabrik Batik X / Sritex Group")
    cek=st.checkbox("Saya Owner Bisnis Pabrik Batik / Konglomerat Batik / Sritex")
    if st.button("BUKA SISTEM OWNER"):
        if cek: st.session_state.owner=True; st.session_state.nama=nama or "Owner Pabrik Batik"; st.rerun()
        else: st.error("Centang verifikasi owner dulu.")
    st.stop()
st.success("Selamat datang Owner | Hero: Turbin DC 1.5 kW dari Uap")
t1,t2,t3,t4=st.tabs(["MODUL 1 — NEURAL: Ruang Analisis","MODUL 2 — CLASSIC: Podcast Intelligent Market","MODUL 3 — TEKNIS PABRIK INFORMATION","MODUL 4 — LAPORAN & AKUNTABILITAS"])
with t1:
    st.subheader("MODUL 1 — NEURAL: Ruang Rakit & Observasi")
    st.write("Merakit, mengobservasi, memverifikasi, memprediksi — sebelum alat dipakai untuk keputusan. Untuk kenyamanan, keamanan, dan pembelajaran dari deteksi sensor.")
    if "heat" not in st.session_state: st.session_state.heat=20; st.session_state.press=0.0; st.session_state.dc=0.0; st.session_state.kain=0; st.session_state.safety=100
    if st.button("Masukkan Kayu Bakar"): st.session_state.heat=min(220,st.session_state.heat+25); st.session_state.press=min(6,st.session_state.press+0.6)
    if st.button("Sirkulasi Uap (Pipa 2-3cm)"): st.session_state.press=min(6,st.session_state.press+0.8)
    if st.button("Aktifkan Turbin DC"): st.session_state.dc=min(1.5, st.session_state.press*0.35)
    if st.button("RELEASE Pluit Safety Guard"): st.session_state.press=max(0,st.session_state.press-2); st.session_state.dc=max(0,st.session_state.dc-0.3)
    lilin=st.slider("Suhu Lilin Parafin + Siongka (C) — Target 90-95, di bawah 100",30,120,90)
    if st.button("Observasi Produksi Batik Mori"):
        st.session_state.kain+=1; st.success("Observasi tercatat. Lilin meresap ke pori Mori jika suhu 90-95C.")
    st.progress(min(st.session_state.press/6,1.0), text=f"Tekanan: {st.session_state.press:.1f} bar")
    st.progress(min(st.session_state.dc/1.5,1.0), text=f"Listrik DC: {st.session_state.dc:.2f} / 1.5 kW")
    st.metric("Hasil Observasi", f"{st.session_state.kain} pcs")
    if st.button("Jalankan Observasi IPAL 3 Bak ke Pemda"): st.info("IPAL: Grease Trap - Netralisasi pH - Filtrasi Multi-Layer - Bak Air Bersih - Pipa IPAL Pemda.")
with t2:
    st.subheader("MODUL 2 — CLASSIC: Podcast Intelligent Market")
    st.write("Siaran bisnis yang menyampaikan hasil observasi seluruh peralatan Pabrik Batik. Terstruktur, beretika, tanpa sensasi.")
    st.markdown("**Episode 1 — Turbin DC 1.5 kW:** Uap dari 2 Tungku Raksasa melalui Kettel 500L menggerakkan turbin, listrik DC untuk kompor lilin di bawah 100C.")
    st.markdown("**Episode 2 — Infrared:** Sensor mendeteksi titik panas di Tungku, Kettel, Kompor. Verifikasi MCB Heavy Industry 50A / 10mm2.")
    st.markdown("**Episode 3 — IPAL:** Limbah melalui 3 bak sebelum ke Pipa IPAL Pemda.")
with t3:
    st.subheader("MODUL 3 — TEKNIS PABRIK INFORMATION")
    st.write("Mencari pangsa market ke setiap Owner Bisnis, meringkas kesimpulan observasi dari Neural. Bukan instruksi beli/jual.")
    st.markdown("**Kesimpulan:** Skenario Utama stabil jika tekanan terjaga, lilin 90-95C, IPAL berjalan. Skenario Alternatif jika tekanan naik, kurangi kayu, aktifkan pluit. Level Invalidasi jika suhu lilin 100C atau lebih.")
with t4:
    st.subheader("MODUL 4 — LAPORAN & AKUNTABILITAS")
    st.write("Laporan berkala, jejak verifikasi, jurnal keputusan, jurnal koreksi, arsip. Semua bisa diaudit oleh pejabat daerah dan pejabat negara.")
    st.table({"Item":["Laporan","Jejak Verifikasi","Jurnal Keputusan","Arsip"],"Isi":["Mingguan/Bulanan","Sumber, Waktu, Verifikator","Kenapa, Risiko, Alternatif","Episode + Laporan"]})
