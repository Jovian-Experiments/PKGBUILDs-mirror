# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=steamos-log-submitter
pkgver=0.2.1
pkgrel=1
pkgdesc="SteamOS Log Submitter"
url="https://gitlab.steamos.cloud/jupiter/steamos-log-submitter"
arch=('any')
license=('LGPL2.1')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamos-log-submitter.git#tag=$pkgver")
sha256sums=('SKIP')
depends=('python' 'python-dbus-next' 'python-httpx' 'python-psutil' 'python-vdf' 'systemd' 'google-breakpad')
makedepends=('git' 'python-setuptools' 'python-wheel' 'python-pip')
checkdepends=('python-pytest' 'python-pytest-asyncio')
conflicts=('breakpad-hook')

package() {
	cd steamos-log-submitter
	make install DESTDIR="$pkgdir"
	pip install --root "$pkgdir" ./
}

check() {
	cd steamos-log-submitter
	dbus-run-session pytest
}
