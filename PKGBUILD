# Maintainer Ethan Geller (ethang@valvesoftware.com)

pkgname=steamdeck-dsp
_srctag=0.86
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
sha512sums=('f3c34526ea90ca1b7e6f1ce985d4b515af80874269196db4aefea6c3622094a822e89545aff65c01ee368dba1e11fd6aa6cd59c45736a055f35e1943c6b2c695')

build() {
  cd valve-hardware-audio-processing
  make FAUSTINC="/usr/include/faust"  FAUSTLIB="/usr/share/faust"
}

package() {
  cd valve-hardware-audio-processing
  make DEST_DIR="$pkgdir/" install
}
