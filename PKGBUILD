pkgname=steamos-repair-backend-git
_tag=20220301.0
pkgver=r27.6823918
pkgrel=2
pkgdesc='Backend web services for steamos-repair tool'
arch=('x86_64')
url='https://gitlab.steamos.cloud/holo/steamos-repair-backend'
license=('GPL')
depends=('bash' 'coreutils' 'util-linux' 'sed' 'file' 'dosfstools' 'e2fsprogs' 'btrfs-progs' 'lighttpd' 'steamos-efi')
makedepends=('git')
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
	autoreconf -vif
	./configure --prefix=/usr --libexecdir=/usr/lib
	make
}

package() {
	cd "${pkgname%-git}"
	make DESTDIR="$pkgdir/" install
}
