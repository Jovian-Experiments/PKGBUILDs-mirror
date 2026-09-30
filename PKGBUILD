# Maintainer: Pierre-Loup A. Griffais (pgriffais@valvesoftware.com)

pkgname=jupiter-hw-support
_srctag=jupiter-20260930.1
_srcver=${_srctag#jupiter-}
pkgver=${_srcver//-/.}
pkgrel=1
arch=('any')
url="https://gitlab.steamos.cloud/jupiter/jupiter-hw-support"
pkgdesc="Jupiter HW support package"
license=('MIT')
depends=('python-evdev'
         'python>=3.14' 'python<3.15'
         'dmidecode' # for jupiter-biosupdate
         'python-crcmod' 'python-click' 'python-progressbar'
         'python-hid>=1.0.6-2' # for jupiter-controller-update
         'jq' # for jupiter-controller-update, jupiter-biosupdate
         'alsa-utils' # for the sound workarounds
         'parted' 'e2fsprogs' # for sdcard formatting
         'udisks2>=2.9.4-1.1' # for mounting external drives with the 'as-user' option
         'holo-plymouth-themes' # for the splash screen when firmware updates on boot up
         'plymouth'             # for the splash screen when firmware updates on boot up
        )
optdepends=('grub-steamos')
makedepends=('rsync' 'git' 'openssh' 'xorg-xcursorgen')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/jupiter-hw-support.git#tag=$_srctag")
sha512sums=('e061f1654408cf64c0267077fd888e999c191359a66b233caeabf35f0ee17473e327f9af824d06b423894f00cd2ed4558b6e911456b5d7dd3225f6973e12c31e')
# Some pre-compiled binaries such as `rfp-cli` break when touched by `strip` :-\
options+=('!strip')

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
