# Maintainer: Simon Hallsten <flightlessmangoyt@gmail.com>

pkgname=rtl88x2ce-dkms
_name=rtl88x2ce
pkgver=5.12.1.6
pkgrel=1
pkgdesc="Realtek RTL88x2CE Driver (DKMS)"
arch=('x86_64' 'i686')
license=('GPL')
depends=('dkms' 'bc')
optdepends=('linux-headers')
provides=('rtl88x2ce')
source=(
	"rtl88x2CE_WiFi_linux_v5.12.1.6-3-gf4aa35fdf.20210730_COEX20210504-2323.tar.gz"
	dkms.conf
	rtw88_blacklist.conf
)
sha256sums=('f7b006410417ab405739af0af78517e2f28c3d4520c7799ccaad5ce0199c4f53'
            '981f31368b09ea28400032d962c5c7c8bb4b8efbc227dfb1ac610cedc9beb7d3'
            'b198a0e866b230f58d2ce9ba0aef221bab823408d040b7aabbac9f26b669ea75')

prepare() {
    cd "$srcdir/rtl88x2CE_WiFi_linux_v5.12.1.6-3-gf4aa35fdf.20210730_COEX20210504-2323"
    sed -i s/GRO_DROP/GRO_MERGED_FREE/ os_dep/linux/recv_linux.c
}

package() {
	cd "$srcdir/rtl88x2CE_WiFi_linux_v5.12.1.6-3-gf4aa35fdf.20210730_COEX20210504-2323"
	mkdir -p "$pkgdir/usr/src/$_name-$pkgver"
	cp -pr * "$pkgdir/usr/src/$_name-$pkgver"
	install -Dm644 "$srcdir/dkms.conf" "$pkgdir/usr/src/$_name-$pkgver/dkms.conf"
	install -Dm644 "$srcdir/rtw88_blacklist.conf" "$pkgdir/usr/lib/modprobe.d/rtw88_blacklist.conf"
	sed -e "s/#MODULE_VERSION#/$pkgver/" -i "$pkgdir/usr/src/$_name-$pkgver/dkms.conf"
}
