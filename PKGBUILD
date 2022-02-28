# Maintainer: Collabora Ltd <gael.portay@collabora.com>

pkgname=steamos-customizations-jupiter
_srctag=jupiter-20220227.1
pkgver=${_srctag#jupiter-}
pkgrel=1
pkgdesc='SteamOS customizations (Jupiter fork) - This package installs various SteamOS-specific files'
arch=('any')
url='http://repo.steampowered.com'
license=('LGPLv2+')
depends=('e2fsprogs' 'gptfdisk' 'rsync' 'util-linux')
makedepends=('git')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=("${pkgname%-git}::git+ssh://git@gitlab.internal.steamos.cloud:/steam/steamos-customizations.git#tag=${_srctag}")
md5sums=('SKIP')

package() {
	cd "${pkgname%-git}"
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" \
		 ATOMUPD_QUERY_URL=https://steamdeck-atomupd.steamos.cloud/updates \
		 ATOMUPD_IMAGES_URL=https://steamdeck-images.steamos.cloud/ \
		 install

	echo "Symlink grub binaries using steamos helpers from libdir..."
	ln -sf "/usr/lib/steamos/steamos-grub-install" "${pkgdir}/usr/bin/grub-install"
	ln -sf "/usr/lib/steamos/steamos-grub-mkimage" "${pkgdir}/usr/bin/grub-mkimage"

	# The desync configs live in separate package
	rm -rf "${pkgdir}/etc/desync"
	# The pacman keyring services live in separate package
	rm -rf "${pkgdir}"/usr/lib/systemd/system/{multi-user.target.wants/,}pacman-{init,cleanup}.service
	# The sudo settings live in separate package
	rm -rf "${pkgdir}/etc/sudoers.d"
}
