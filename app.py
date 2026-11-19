# Pabrik Batik Autonomous - Sales Demand Planner + Infrared
# Owner Only: Pabrik Batik / Konglomerat Batik / Sritex
# Fungsi sama dengan repo supersecure, produk diganti khusus pabrik
def demand_planner(bahan):
    return {'Mori Primis': 'input gudang besar', 'Lilin Parafin+Siongka': 'kompor <100C', 'Pewarna Reaktif': 'celup warna'}.get(bahan, 'input')

def infrared_scan(titik):
    return f'Scan {titik}: panas terdeteksi, buka kartu peralatan'

if __name__ == '__main__':
    print('Pabrik Batik Autonomous - Owner Only - jalan')
