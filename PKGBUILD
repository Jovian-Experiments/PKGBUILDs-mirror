# Maintainer Ethan Geller (ethang@valvesoftware.com)

pkgname=steamdeck-dsp
_srctag=0.71
pkgver=${_srctag#galileo-}
pkgrel=2
arch=('any')
url=""
pkgdesc="Steamdeck Audio Processing"
license=('Proprietary')
depends=('pipewire' 'pipewire-audio' 'noisetorch')
makedepends=('git' 'openssh' 'base-devel' 'glibc' 'faust' 'ladspa' 'lv2' 'boost' 'linux-api-headers' 'qt5-base')
install="${pkgname}.install"
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/valve-hardware-audio-processing.git#tag=$_srctag")
sha512sums=('b4f2fa2651b75adb1cc8bc395b017692ad87899c9c690e5360429a5d5b1603ee159b1e679d823a33f4cfef1996793d7cccb64ba4ed3bbd95a3637e66f12d9dec')

build() {
  cd valve-hardware-audio-processing
  make FAUSTINC="/usr/include/faust"  FAUSTLIB="/usr/share/faust"
}

package() {
  cd valve-hardware-audio-processing
  make DEST_DIR="$pkgdir/" install
}
