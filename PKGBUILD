# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=steamos-log-submitter
pkgver=0.5.0
pkgrel=2
pkgdesc="SteamOS Log Submitter"
url="https://gitlab.steamos.cloud/jupiter/steamos-log-submitter"
arch=('any')
license=('LGPL2.1')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamos-log-submitter.git#tag=$pkgver"
        '0001-helpers-trace-Disable-by-default.patch')
sha256sums=('SKIP'
            'af11c5de4395ac83596becefd9f2ad8c9f5564f2830c555157f0c593af075224')
depends=('python' 'python-dbus-next' 'python-httpx' 'python-psutil' 'python-pyalsa' 'python-pyelftools' 'systemd' 'google-breakpad')
makedepends=('git' 'python-setuptools' 'python-wheel' 'python-pip')
checkdepends=('python-pytest' 'python-pytest-asyncio')
conflicts=('breakpad-hook')

prepare() {
	patch -d steamos-log-submitter -p1 < 0001-helpers-trace-Disable-by-default.patch
}

package() {
	cd steamos-log-submitter
	make install DESTDIR="$pkgdir"
	pip install --root "$pkgdir" ./
}

check() {
	cd steamos-log-submitter
	dbus-run-session pytest
}
