# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=usbhid-gadget-passthru
_srctag=0.1.3
pkgver=${_srctag}
pkgrel=5
pkgdesc="USB HID device passthrough via gadget subsystem"
url="https://gitlab.steamos.cloud/endrift/usbhid-gadget-passthru"
arch=('x86_64')
license=('BSD')
source=("git+ssh://git@gitlab.steamos.cloud/endrift/usbhid-gadget-passthru.git#tag=v${_srctag}"
        "polkit.actions"
        "0001-Remove-D_FORTIFY_SOURCE.patch"

        # Backport of https://gitlab.steamos.cloud/endrift/usbhid-gadget-passthru/-/merge_requests/1
        "6ddb62ef5babfda48f85ce97a73176b488d63d37.patch")
sha256sums=('681fa9f350939a78f6c7d31ed3b326de769a303fdb83b627997316fffccf7836'
            'd8f3bfc459651762b2435d6a4ea22cdeb7f739e2a8679b09fe7f38a38b0b2121'
            '07cf37b9abed95266d6629cfd098abc3c5da98f3fe736968b5b47c77acb74fef'
            '1545fc6a6beefbe729a600e7e8a1cbd587b0b1b02367452d8f06fc4ce94d3ad1')
depends=('glibc')
makedepends=('linux-api-headers' 'git' 'openssh')

prepare() {
	cd "$pkgname"
	patch -Np1 < "$srcdir/0001-Remove-D_FORTIFY_SOURCE.patch"
	patch -Np1 < "$srcdir/6ddb62ef5babfda48f85ce97a73176b488d63d37.patch"
}

package() {
	install -m644 -D polkit.actions "${pkgdir}/usr/share/polkit-1/actions/com.steampowered.usbhid-gadget-passthru.policy"

	cd "$pkgname"
	make install DESTDIR="$pkgdir"
	install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
