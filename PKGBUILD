# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=usbhid-gadget-passthru
_srctag=0.1.3
pkgver=${_srctag}
pkgrel=2
pkgdesc="SteamOS Log Submitter"
url="https://gitlab.steamos.cloud/endrift/usbhid-gadget-passthru"
arch=('x86_64')
license=('BSD')
source=("git+ssh://git@gitlab.steamos.cloud/endrift/usbhid-gadget-passthru.git#tag=v${_srctag}"
        "polkit.actions")
sha256sums=('SKIP'
            'd8f3bfc459651762b2435d6a4ea22cdeb7f739e2a8679b09fe7f38a38b0b2121')
depends=('glibc')
makedepends=('linux-api-headers' 'git' 'openssh')

package() {
	install -m644 -D polkit.actions "${pkgdir}/usr/share/polkit-1/actions/com.steampowered.usbhid-gadget-passthru.policy"

	cd "$pkgname"
	make install DESTDIR="$pkgdir"
	install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
