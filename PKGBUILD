# Maintainer: Collabora Ltd <gael.portay@collabora.com>

pkgbase=steamos-customizations-git
#pkgname=('steamos-customizations-git' 'holo-desync' 'holo-pacman' 'holo-pipewire' 'holo-sudo' 'holo-wireplumber')
pkgname=('steamos-customizations-git' 'holo-desync' 'holo-pipewire' 'holo-sudo' 'holo-wireplumber')
_srctag=jupiter-20230424.1
_srcver=${_srctag#jupiter-}
pkgver=r767.3e6b56b
pkgrel=1
pkgdesc='SteamOS customizations - This package installs various SteamOS-specific files'
arch=('any')
url='http://repo.steampowered.com'
license=('LGPLv2+')
depends=('e2fsprogs' 'gptfdisk' 'rsync' 'util-linux')
makedepends=('git')
source=("${pkgbase%-git}::git+https://gitlab.steamos.cloud/steam/${pkgbase%-git}.git#tag=${_srctag}")
md5sums=('SKIP')

pkgver() {
	cd "${pkgbase%-git}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package_steamos-customizations-git() {
	provides=("${pkgbase%-git}")
	conflicts=("${pkgbase%-git}")

	cd "${pkgbase%-git}"
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" install

	echo "Symlink grub binaries using steamos helpers from libdir..."
	ln -sf "/usr/lib/steamos/steamos-grub-install" "${pkgdir}/usr/bin/grub-install"
	ln -sf "/usr/lib/steamos/steamos-grub-mkimage" "${pkgdir}/usr/bin/grub-mkimage"
}

package_holo-desync() {
	pkgdesc='Holo customizations - desync configuration'
	depends=()
	groups=(holo-base)

	cd "${pkgbase%-git}"
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" install-desync
}

package_holo-pacman() {
	pkgdesc='Holo customizations - pacman keyring services'
	depends=()
	groups=(holo-base)

	cd "${pkgbase%-git}"
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" install-pacman
}

package_holo-pipewire() {
	pkgdesc='Holo customizations - pipewire settings'
	depends=()
	groups=(holo-base)

	cd "${pkgbase%-git}"
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" install-pipewire
}

package_holo-sudo() {
	pkgdesc='Holo customizations - sudo settings'
	depends=()
	groups=(holo-base)

	cd "${pkgbase%-git}"
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" install-sudo
}

package_holo-wireplumber() {
	pkgdesc='Holo customizations - wireplumber settings'
	depends=()
	groups=(holo-base)

	cd "${pkgbase%-git}"
	make DESTDIR="$pkgdir" prefix="/usr" sbindir="/usr/bin" libexecdir="/usr/lib" install-wireplumber
}
