# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=steamos-log-submitter
pkgver=0.1.1
pkgrel=4
pkgdesc="SteamOS Log Submitter"
url="https://gitlab.steamos.cloud/jupiter/steamos-log-submitter"
arch=('any')
license=('LGPL2.1')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/steamos-log-submitter.git#tag=$pkgver"
        "0001-Fix-systemd-symlink-path.patch")
sha256sums=('SKIP'
            'eb8b065afb19d35ca4d59d4da842f8a943ee8f5fb01c3b7fd0dc814707d8f3fb')
depends=('python' 'python-dbus-next' 'python-httpx' 'python-psutil' 'python-vdf' 'systemd' 'google-breakpad')
makedepends=('git' 'python-setuptools' 'python-wheel' 'python-pip')
checkdepends=('python-pytest' 'python-pytest-asyncio')
conflicts=('breakpad-hook')

package() {
	cd steamos-log-submitter
	patch -p1 < "$srcdir/0001-Fix-systemd-symlink-path.patch"
	make install DESTDIR="$pkgdir"
	pip install --root "$pkgdir" ./
}

check() {
	cd steamos-log-submitter
	dbus-run-session pytest
}
