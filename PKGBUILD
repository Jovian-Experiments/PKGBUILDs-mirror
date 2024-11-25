# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=usbhid-gadget-passthru
_srctag=0.1.3
pkgver=${_srctag}
pkgrel=4
pkgdesc="USB HID device passthrough via gadget subsystem"
url="https://gitlab.steamos.cloud/endrift/usbhid-gadget-passthru"
arch=('x86_64')
license=('BSD')
source=("git+ssh://git@gitlab.steamos.cloud/endrift/usbhid-gadget-passthru.git#tag=v${_srctag}"
        "polkit.actions"
        "0001-Remove-D_FORTIFY_SOURCE.patch")
sha256sums=('SKIP'
            'd8f3bfc459651762b2435d6a4ea22cdeb7f739e2a8679b09fe7f38a38b0b2121'
            '07cf37b9abed95266d6629cfd098abc3c5da98f3fe736968b5b47c77acb74fef')
depends=('glibc')
makedepends=('linux-api-headers' 'git' 'openssh')

prepare() {
	cd "$pkgname"
	patch -Np1 < "$srcdir/0001-Remove-D_FORTIFY_SOURCE.patch"
}

package() {
	install -m644 -D polkit.actions "${pkgdir}/usr/share/polkit-1/actions/com.steampowered.usbhid-gadget-passthru.policy"

	cd "$pkgname"
	make install DESTDIR="$pkgdir"
	install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
