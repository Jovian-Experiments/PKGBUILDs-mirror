# Maintainer Ethan Geller (ethang@valvesoftware.com)

pkgname=steamdeck-dsp
_srctag=0.68
pkgver=${_srctag#galileo-}
pkgrel=1
arch=('any')
url=""
pkgdesc="Steamdeck Audio Processing"
license=('Proprietary')
depends=('pipewire')
makedepends=('git' 'openssh' 'base-devel' 'glibc' 'faust' 'ladspa' 'lv2' 'boost' 'linux-api-headers' 'qt5-base')
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/valve-hardware-audio-processing.git#tag=$_srctag")
sha512sums=('298ea6db0af20a6a3207d870e892440c03e6607eaae3ea87eb361c36fc2c44be81e1b185deb734a82c086e733bc302106d20ec6e4409ba434699ef183b0a62ae')

build() {
  cd valve-hardware-audio-processing
  make FAUSTINC="/usr/include/faust"  FAUSTLIB="/usr/share/faust"
}

package() {
  cd valve-hardware-audio-processing
  make DEST_DIR="$pkgdir/" install
}
