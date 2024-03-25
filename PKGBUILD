pkgname=steamos-repair-tool-git
_tag=20220301
pkgver=r17.7783747
pkgrel=3
pkgdesc='CEF application to allow user to recover steamos image'
arch=('x86_64')
url='https://gitlab.steamos.cloud/holo/steamos-repair-tool'
license=('GPL')
# XXX: Do a double-take on these deps, they seem iffy
depends=('libxkbcommon' 'cups' 'nss' 'alsa-lib' 'at-spi2-atk' 'pango' 'libxrandr' 'libxcursor' 'libxss' 'libxtst' 'libxcomposite' 'libglvnd' 'dbus')
makedepends=('git' 'tar' 'cmake')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")

source=("${pkgname%-git}::git+${url}#tag=${_tag}")
sha256sums=('SKIP')

pkgver() {
	cd "${pkgname%-git}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "${pkgname%-git}"
	mkdir build
	cmake -S cef_app/ -B build/
	make -C build
}

package() {
	cd "${pkgname%-git}"

	install -dm 755 "$pkgdir/usr"
	cp -av ./build/Release/* "$pkgdir/usr/"
}
