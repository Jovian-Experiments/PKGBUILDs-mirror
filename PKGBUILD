# Maintainer: Ludovico de Nittis <ludovico.denittis@collabora.com>
# Maintainer: Vivek Das Mohapatra <vivek.dasmohapatra@collabora.com>

pkgname=steamos-customizations-jupiter
_srctag=jupiter-20260914.1
_srcver=${_srctag#jupiter-}
pkgver=${_srcver//-/.}
pkgrel=1
pkgdesc='SteamOS customizations (Jupiter fork) - This package installs various SteamOS-specific files'
arch=('any')
url='http://repo.steampowered.com'
license=('LGPLv2+')
depends=('e2fsprogs' 'gptfdisk' 'rsync' 'util-linux' 'mkinitcpio')
makedepends=('git' 'openssh' 'systemd')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=("${pkgname%-git}::git+ssh://git@gitlab.steamos.cloud/holo/steamos-customizations.git#tag=${_srctag}")
sha256sums=('0d53c1a815adb56e7c7eee5ebb1f899115ea08a253d769a41f470511715ed8a0')

package() {
	cd "${pkgname%-git}"
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" \
		 ATOMUPD_META_URL=https://steamdeck-atomupd.steamos.cloud/meta \
		 ATOMUPD_IMAGES_URL=https://steamdeck-images.steamos.cloud/ \
		 ATOMUPD_VARIANTS_LIST='steamdeck' \
		 ATOMUPD_BRANCHES_LIST='stable;rc;beta;bc;preview;pc;main' \
		 install
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" -C mkinitcpio install

	echo "Symlink grub binaries using holo helpers from libdir..."
	ln -sf "/usr/lib/holo/holo-grub-install" "${pkgdir}/usr/bin/grub-install"
	ln -sf "/usr/lib/holo/holo-grub-mkimage" "${pkgdir}/usr/bin/grub-mkimage"

	# The pacman keyring services live in separate package
	rm -rf "${pkgdir}"/usr/lib/systemd/system/{multi-user.target.wants/,}pacman-{init,cleanup}.service
}
