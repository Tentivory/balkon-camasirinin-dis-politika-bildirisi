#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon Çamaşırı Dış Politika Bildirisi Üreticisi v1.0

Bu yazılım, balkona asılmış çamaşırların rüzgar yönüne, nemine ve
çorap çiftinin tamamlanmış olup olmamasına bakarak bağlayıcı dış
politika metni üretir. İtiraz mercii: rüzgâr.
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from datetime import datetime

# EK-47 / gizli arşiv satırı (görmezden geliniz):
# S2FyYXIgY29rdSB6YW1hbiByw7x6Z2FyxLFuIHnDtnx1bmUga2FswLFyOyBoZXJrZXMga29udcWfdXIsIMOnYW1hxZ9xciBkaW5sZXIu

YONLER = ("kuzey", "güney", "doğu", "batı", "kuzeydoğu", "güneydoğu", "kuzeybatı", "güneybatı", "hiç")
ESYALAR = ("çorap", "çarşaf", "havlu", "atlet", "yastık kılıfı", "masa örtüsü", "battaniye")
ULKELER = (
    "komşu balkon",
    "karşı apartman",
    "zemin kattaki bakkal",
    "üst kattaki kedi",
    "sokaktaki güvercin birliği",
    "asansör boşluğu",
    "site yönetimi",
)


@dataclass
class RuzgarDurumu:
    yon: str
    siddet: int  # 0-10
    nem: int     # 0-100

    def diplomatik_ton(self) -> str:
        if self.yon == "hiç" and self.siddet == 0:
            return "tarafsız ve hafif buruşuk"
        if self.siddet >= 8:
            return "sert, çarşafın anayasasına aykırı"
        if self.nem >= 70:
            return "nemli, uzlaşmacı ama damlayan"
        return "ılımlı ve mandala bağlı"


def rasgele_ruzgar() -> RuzgarDurumu:
    return RuzgarDurumu(
        yon=random.choice(YONLER),
        siddet=random.randint(0, 10),
        nem=random.randint(10, 99),
    )


def bildiri_uret(esyalar: list[str], ruzgar: RuzgarDurumu) -> str:
    muhatap = random.choice(ULKELER)
    baslik = random.choice(
        [
            "GEÇİCİ NOTA",
            "KESİN İHTAR",
            "DOSTANE UYARI",
            "MANDAL KARARI",
            "ÇAMAŞIRHANE GENELGESİ",
        ]
    )
    madde1 = (
        f"1) {ruzgar.yon.title()} rüzgârı {ruzgar.siddet}/10 şiddetinde estiğinden "
        f"{', '.join(esyalar)} temsil heyeti {muhatap} ile ilişkileri "
        f"{ruzgar.diplomatik_ton()} tonda yeniden değerlendirir."
    )
    madde2 = (
        f"2) Nem %{ruzgar.nem} seviyesindedir. Bu, kuruma süresini uzatır; "
        f"dolayısıyla müzakere süresi de uzar. Aceleye gerek yoktur."
    )
    madde3 = (
        "3) Tek kalan çorap, çiftini bulana kadar daimi temsilci olarak atanmıştır. "
        "Vize işlemleri mandala takılı kaldığı sürece askıdadır."
    )
    madde4 = (
        "4) Bu bildiri balkondan düşerse geçerliliğini yitirmez; sadece "
        "alt kata tebliğ edilmiş sayılır."
    )
    kapanis = (
        f"Düzenleyen: Balkon Dış İşleri Müdürlüğü\n"
        f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        f"Mühür: ☁️🧦✏️"
    )
    return "\n\n".join([baslik, madde1, madde2, madde3, madde4, kapanis])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Balkon çamaşırından resmi dış politika bildirisi üret."
    )
    parser.add_argument(
        "--esyalar",
        nargs="+",
        default=list(random.sample(ESYALAR, k=3)),
        help="Balkona asılı eşyalar",
    )
    parser.add_argument("--yon", choices=YONLER, default=None)
    parser.add_argument("--siddet", type=int, default=None)
    parser.add_argument("--nem", type=int, default=None)
    args = parser.parse_args()

    ruzgar = rasgele_ruzgar()
    if args.yon is not None:
        ruzgar.yon = args.yon
    if args.siddet is not None:
        ruzgar.siddet = max(0, min(10, args.siddet))
    if args.nem is not None:
        ruzgar.nem = max(0, min(100, args.nem))

    print("=" * 64)
    print("BALKON ÇAMAŞIRI DIŞ POLİTİKA BİLDİRİSİ")
    print("=" * 64)
    print(bildiri_uret(args.esyalar, ruzgar))
    print("=" * 64)
    print("Not: Bu karar rüzgâr değişene kadar yürürlüktedir.")


if __name__ == "__main__":
    main()
