# Maintainer: Collabora Ltd <gael.portay@collabora.com>

pkgname=kupdate-notifier-git
pkgver=r59.7e34c35
pkgrel=4
pkgdesc='Update Notifier for the new systemtray specification.'
arch=('x86_64')
url='http://repo.steampowered.com'
license=('LGPL2.1')
depends=('knotifications'
         'qt5-tools' # for qdbus used in kupdate-notifier.action
        )
makedepends=('git' 'knotifications' )
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=("${pkgname%-git}::git+https://gitlab.steamos.cloud/steam/${pkgname%-git}.git#commit=7e34c35")
md5sums=('SKIP')

pkgver() {
	cd "${pkgname%-git}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "${pkgname%-git}"
	make
}

package() {
	cd "${pkgname%-git}"
	make DESTDIR="$pkgdir" PREFIX="/usr" install
	install -D -m 644 bash-completion "$pkgdir/usr/share/bash-completion/completions/${pkgname%-git}"
	install -D -m 644 LICENSE "$pkgdir/usr/share/licenses/${pkgname%-git}/LICENSE"
}
