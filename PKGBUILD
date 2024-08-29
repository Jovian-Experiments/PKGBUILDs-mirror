# Maintainer: Ludovico de Nittis <ludovico.denittis@collabora.com>

pkgname=steamos-atomupd-client
pkgver=0.20240827.1
pkgrel=1
pkgdesc='SteamOS Atomic Update (client) - Atomic update client for SteamOS.'
arch=('any')
url='https://store.steampowered.com/steamos/'
license=('LGPL2.1')
makedepends=('git')
depends=('python>=3.11' 'python<3.12' 'rauc' 'python-semantic-version')
optdepends=('desync')
provides=("${pkgname}")
conflicts=("${pkgname}")
source=("${pkgname}::git+https://gitlab.steamos.cloud/holo/${pkgname%-client}.git#tag=v${pkgver}")
md5sums=('SKIP')

build() {
	cd "${pkgname}"
	python setup.py build
}

package () {
	cd "${pkgname}"

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
