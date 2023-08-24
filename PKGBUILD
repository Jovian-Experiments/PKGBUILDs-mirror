# Maintainer: Collabora Ltd <gael.portay@collabora.com>

pkgname=steamos-efi
_srctag=jupiter-20230823.1
pkgver=${_srctag#jupiter-}
pkgrel=1
arch=('x86_64')
url='https://gitlab.steamos.cloud/steam/steamos-efi'
pkgdesc='Stage 1 bootloader for SteamOS 3+'
license=('GPL2')
depends=('efibootmgr' 'util-linux' 'coreutils')
makedepends=('git' 'openssh' 'gnu-efi-libs')
source=("git+ssh://git@gitlab.steamos.cloud/steam/${pkgname}.git#tag=$_srctag")
sha512sums=('SKIP')

build() {
	cd "${pkgname}"
	autoreconf -vif
	./configure --prefix=/usr --with-release-version="$pkgver"
	make
}

package() {
	cd "${pkgname}"
	make DESTDIR="$pkgdir/" install
	mv "$pkgdir/usr/sbin/"* "$pkgdir/usr/bin/"
	rmdir "$pkgdir/usr/sbin/"
}
