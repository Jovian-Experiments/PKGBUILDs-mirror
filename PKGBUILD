# Maintainer: Thomas Bächler <thomas@archlinux.org>

pkgbase=linux-firmware-neptune
pkgname=(linux-firmware-neptune-rtw-debug) # amd-ucode)
_tag=jupiter-20220524-rtw-debug
_srctag=${_tag#jupiter-}
pkgver=${_srctag%-rtw-debug}
pkgrel=1
pkgdesc="Firmware files for Linux"
url="https://gitlab.steamos.cloud/jupiter/linux-firmware-neptune"
license=('GPL2' 'GPL3' 'custom')
arch=('any')
makedepends=('git')
options=(!strip !debug)
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/linux-firmware-neptune.git#tag=$_tag")
sha256sums=('SKIP')
validpgpkeys=('4CDE8575E547BF835FE15807A31B6BD72486CFD6') # Josh Boyer <jwboyer@fedoraproject.org>

_backports=(
)

prepare() {
  cd ${pkgbase}

  local _c
  for _c in "${_backports[@]}"; do
    git log --oneline -1 "${_c}"
    git cherry-pick -n "${_c}"
  done
}

build() {
  mkdir -p kernel/x86/microcode
  cat ${pkgbase}/amd-ucode/microcode_amd*.bin > kernel/x86/microcode/AuthenticAMD.bin

  # Reproducibility: set the timestamp on the bin file
  if [[ -n ${SOURCE_DATE_EPOCH} ]]; then 
    touch -d @${SOURCE_DATE_EPOCH} kernel/x86/microcode/AuthenticAMD.bin
  fi

  # Reproducibility: strip the inode and device numbers from the cpio archive
  echo kernel/x86/microcode/AuthenticAMD.bin |
    bsdtar --uid 0 --gid 0 -cnf - -T - |
    bsdtar --null -cf - --format=newc @- > amd-ucode.img
}

package_linux-firmware-neptune-rtw-debug() {
  provides=('linux-firmware')
  conflicts=('linux-firmware')
  replaces=('linux-firmware')

  cd ${pkgbase}

  make DESTDIR="${pkgdir}" FIRMWAREDIR=/usr/lib/firmware install

  # Trigger a microcode reload for configurations not using early updates
  echo 'w /sys/devices/system/cpu/microcode/reload - - - - 1' |
    install -Dm644 /dev/stdin "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"

  install -Dt "${pkgdir}/usr/share/licenses/${pkgname}" -m644 LICEN* WHENCE

  # Jupiter: remove unused/unneeded firmware files, bloating the package.
  # Listed in decreasing size, mainly server NIC and non-AMD gpu
  local -r _unused_firmware="netronome qcom mellanox liquidio qed i915 dpaa2 radeon nvidia"
  for folder in ${_unused_firmware}; do
    rm -rf "${pkgdir}/usr/lib/firmware/$folder"
  done

  # In addition, nuke all amdgpu firmware but VanGogh which we need
  for amdgpu in "${pkgdir}/usr/lib/firmware/amdgpu/"*; do
    _file=$(basename $amdgpu)
    [[ "$_file" = vangogh* ]] && continue
    rm -rf "$amdgpu"
  done
}

package_amd-ucode() {
  pkgdesc="Microcode update image for AMD CPUs"
  license=(custom)

  install -Dt "${pkgdir}/boot" -m644 amd-ucode.img

  install -Dt "${pkgdir}/usr/share/licenses/${pkgname}" -m644 ${pkgbase}/LICENSE.amd-ucode
}

# vim:set sw=2 et:
