# Maintainer: Pierre-Loup A. Griffais (pgriffais@valvesoftware.com)

pkgname=jupiter-hw-support
_srctag=jupiter-20220719.01
_srcver=${_srctag#jupiter-}
pkgver=${_srcver//-/.}
pkgrel=2
arch=('any')
url="https://gitlab.steamos.cloud/jupiter/jupiter-hw-support"
pkgdesc="Jupiter HW support package"
license=('MIT')
depends=('python-evdev'
         'dmidecode' # for jupiter-biosupdate
         'python-crcmod' 'python-click' 'python-progressbar' 'python-hid'
         'jq' # for jupiter-controller-update, jupiter-biosupdate
         'alsa-utils' # for the sound workarounds
         'parted' 'e2fsprogs' # for sdcard formatting
        )
optdepends=('grub-steamos')
makedepends=('rsync' 'git' 'xorg-xcursorgen')
source=("git+ssh://git@gitlab.internal.steamos.cloud/jupiter/jupiter-hw-support.git#tag=$_srctag")
sha512sums=(SKIP)

package() {
  rsync -a "$srcdir"/jupiter-hw-support/* "$pkgdir"

  cd $pkgdir/usr/share/steamos/
  xcursorgen $pkgdir/usr/share/steamos/steamos-cursor-config $pkgdir/usr/share/icons/steam/cursors/default

  cd "$pkgdir/usr/share/jupiter_bios_updater"

  # Remove gtk2 binary and respective build/start script - unused
  # Attempts to use gtk2 libraries which are not on the device.
  rm h2offt-g H2OFFTx64-G.sh

  # Driver module -- doesn't currently build, and not supported
  rm -rf driver
}
