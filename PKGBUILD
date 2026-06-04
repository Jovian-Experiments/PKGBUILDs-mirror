# Maintainer Ethan Geller (ethang@valvesoftware.com)

pkgname=steamdeck-dsp
_srctag=0.94
pkgver=${_srctag#galileo-}
pkgrel=1
arch=('any')
url=""
pkgdesc="Steamdeck Audio Processing"
license=('Proprietary')
depends=('pipewire' 'pipewire-audio' 'noisetorch')
makedepends=('git' 'openssh' 'base-devel' 'glibc' 'faust' 'ladspa' 'lv2' 'boost' 'linux-api-headers' 'qt5-base')
install="${pkgname}.install"
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/valve-hardware-audio-processing.git#tag=$_srctag")
sha512sums=('e1ab6835c37a624b4a56b59af48454794dbb9555d106761b856d7c7a6c073f13963dc593260ab8ca1e97bfa012cd85b07dd30b8b954a96c5e015686f0e509c5a')

build() {
  cd valve-hardware-audio-processing
  make FAUSTINC="/usr/include/faust"  FAUSTLIB="/usr/share/faust"
}

package() {
  cd valve-hardware-audio-processing
  make DEST_DIR="$pkgdir/" install
}
