# Maintainer: Gaël PORTAY <gael.portay@collabora.com>

pkgname=steamos-atomupd-client-git
_srctag=v0.20230609.0
pkgver=r301.e0c2c4d
pkgrel=3
pkgdesc='SteamOS Atomic Update (client) - Atomic update client for SteamOS.'
arch=('any')
url='https://store.steampowered.com/steamos/'
license=('LGPL2.1')
makedepends=('git')
depends=('python' 'rauc' 'python-semantic-version')
optdepends=('desync')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=("${pkgname%-git}::git+https://gitlab.steamos.cloud/holo/${pkgname%-client-git}.git#tag=${_srctag}")
md5sums=('SKIP')

pkgver() {
	cd "${pkgname%-git}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "${pkgname%-git}"
	python setup.py build
}

package () {
	cd "${pkgname%-git}"

	python setup.py install --root="$pkgdir/" --optimize=1 --skip-build

	install -Dm755 "bin/steamos-atomupd-client" "$pkgdir/usr/bin/steamos-atomupd-client"
	install -Dm755 "bin/steamos-atomupd-mkmanifest" "$pkgdir/usr/bin/steamos-atomupd-mkmanifest"
	install -Dm644 "completions/steamos-atomupd-client" "$pkgdir/usr/share/bash-completion/completions/steamos-atomupd-client"
	install -Dm644 "completions/steamos-atomupd-mkmanifest" "$pkgdir/usr/share/bash-completion/completions/steamos-atomupd-mkmanifest"
	install -dm755 "$pkgdir/usr/lib/steamos-atomupd"
	install -dm755 "$pkgdir/etc/steamos-atomupd"
	install -Dm644 "examples/client.conf" "$pkgdir/usr/share/steamos-atomupd-client/examples/client.conf"
	install -Dm644 "examples/image.manifest.json" "$pkgdir/usr/share/steamos-atomupd-client/examples/image.manifest.json"
}
