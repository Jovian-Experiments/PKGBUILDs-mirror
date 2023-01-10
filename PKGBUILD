# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=usbhid-gadget-passthru
_srctag=0.1.1
pkgver=${_srctag}
pkgrel=1
pkgdesc="SteamOS Log Submitter"
url="https://gitlab.steamos.cloud/endrift/usbhid-gadget-passthru"
arch=('x86_64')
license=('BSD')
source=("git+ssh://git@gitlab.steamos.cloud/endrift/usbhid-gadget-passthru.git#tag=v${_srctag}")
sha256sums=('SKIP')
depends=('glibc')
makedepends=('linux-api-headers' 'git' 'openssh')

package() {
	cd "$pkgname"
	make install DESTDIR="$pkgdir"
	install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
