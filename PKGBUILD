# Maintainer Ethan Geller (ethang@valvesoftware.com)

pkgname=steamdeck-dsp
_srctag=0.70
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
sha512sums=('aeb3b3f1e5c1bb229d492a87a364bb87afbd5a6bee3f0dab552336a44fa1292f1b4eea3c156185394b1b9cb207ff695f3439a3e395f45fa3cc006d0360d36dd2')

build() {
  cd valve-hardware-audio-processing
  make FAUSTINC="/usr/include/faust"  FAUSTLIB="/usr/share/faust"
}

package() {
  cd valve-hardware-audio-processing
  make DEST_DIR="$pkgdir/" install
}
