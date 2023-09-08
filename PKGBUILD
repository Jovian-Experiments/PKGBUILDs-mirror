# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=jupiter-steamos-log-submitter
pkgver=1
pkgrel=1
pkgdesc="SteamOS Log Submitter - Jupiter support"
url="https://gitlab.steamos.cloud/jupiter/steamos-log-submitter"
arch=('any')
license=('LGPL2.1')
source=('var-lib-steamos-log-submitter.mount'
        'sysusers.conf')
sha256sums=('7d42ebc9e6d7cb0e89ef0116312b10a7f6d6cca1fd6ca573207a7a8e87a8c20f'
            '8e4f8d054d21c13a03ccc7038109a3364ca5adfa16da3368bc84aa741387a8f4')
depends=('steamos-log-submitter')

package() {
	install -D -m0644 sysusers.conf "$pkgdir/usr/lib/sysusers.d/jupiter-steamos-log-submitter.conf"
	install -D -m0644 var-lib-steamos-log-submitter.mount "$pkgdir/usr/lib/systemd/system/var-lib-steamos\\x2dlog\\x2dsubmitter.mount"

	mkdir -p -m0755 "$pkgdir/usr/lib/systemd/system/steamos-offload.target.wants"
	(cd "$pkgdir/usr/lib/systemd/system/steamos-offload.target.wants" && ln -sf ../var-lib-steamos\\x2dlog\\x2dsubmitter.mount)

	mkdir -p -m0755 "$pkgdir/usr/lib/systemd/system/steamos-log-submitter.service.requires"
	(cd "$pkgdir/usr/lib/systemd/system/steamos-log-submitter.service.requires" && ln -sf ../var-lib-steamos\\x2dlog\\x2dsubmitter.mount)
}
