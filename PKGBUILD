# Maintainer: Collabora Ltd <gael.portay@collabora.com>

pkgname=calamares
pkgver=3.2.37
#patch applied to disable btrfs creating subvolumes. Remove patch
#once https://gitlab.steamos.cloud/holo/tasks/-/issues/49 is fixed.
pkgrel=6
epoch=1
pkgdesc='Distribution-independent installer framework'
arch=('i686' 'x86_64')
url='https://calamares.io/'
license=('GPL')
depends=('ckbcomp' 'kconfig' 'kcoreaddons' 'kiconthemes' 'ki18n' 'kio' 'solid' 'yaml-cpp' 'kpmcore'
         'boost-libs' 'hwinfo' 'qt5-svg' 'polkit-qt5' 'gtk-update-icon-cache' 'plasma-framework'
         'qt5-xmlpatterns' 'squashfs-tools')
makedepends=('extra-cmake-modules' 'qt5-tools' 'qt5-translations' 'git' 'boost')
backup=('usr/share/calamares/modules/bootloader.conf'
        'usr/share/calamares/modules/displaymanager.conf'
        'usr/share/calamares/modules/initcpio.conf'
        'usr/share/calamares/modules/unpackfs.conf')
source=("git+https://github.com/calamares/calamares.git#tag=v$pkgver"
        "0004-unpackfs-Use-rsync-option-S.patch"
        "0001-Disable-subvolume-creation.patch"
        'com.github.Calamares.rules')
sha256sums=('SKIP'
            '2f53f46b2105cb66b3d9e61c45958ab5de0a10516c017875a0d5a8e47ab3a1d5'
            'bb48bf1d4934bfcd51ddc001df39868137f89aeb8c091ecc209918710596d4c7'
            '57bc5f5069e5415bc32418dbbc7f49d499b7f50da9eb782aa0de65b2824b9dff')

prepare() {
	cd "${pkgname}"

	patch -p1 -i "${srcdir}/0004-unpackfs-Use-rsync-option-S.patch"
	# btrfs: Disable creation of subvolumes for btrfs.
	# Remove it once we have migrate to latest upstream which
	# already have handling for this
	patch -p1 -i "${srcdir}/0001-Disable-subvolume-creation.patch"
}

build() {
	cd "${pkgname}"

	mkdir -p build
	cd build
	cmake .. \
	      -DCMAKE_BUILD_TYPE=Release \
	      -DCMAKE_INSTALL_PREFIX=/usr \
	      -DCMAKE_INSTALL_LIBDIR=lib \
	      -DBoost_NO_BOOST_CMAKE=ON \
	      -DINSTALL_COMPLETION=ON
	make
}

package() {
	cd "${pkgname}/build"
	make DESTDIR="$pkgdir" install
	rm -f "$pkgdir/usr/share/applications/calamares.desktop"
	install -d -m750 "$pkgdir/usr/share/polkit-1/rules.d/"
	install -D -m644 "$srcdir/com.github.Calamares.rules" "$pkgdir/usr/share/polkit-1/rules.d/com.github.Calamares.rules"
}
