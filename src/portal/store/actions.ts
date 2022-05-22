import { PortalState } from './state';
import type { ActionContext } from "vuex";
import {
   web3Enable,web3AccountsSubscribe

  } from '@polkadot/extension-dapp';


export default{
   
    async subscribeAccounts({commit}: ActionContext<PortalState, PortalState>){
            await web3Enable('TF Chain UI')
            await web3AccountsSubscribe(( injectedAccounts ) => { 
                commit('setAccounts', { accounts: injectedAccounts })
        })

    },
    async unsubscribeAccounts({commit}:ActionContext<PortalState, PortalState> ){
        const unsubscribe = await web3AccountsSubscribe(( ) => { 
            console.log(`unsubscribing`)
        });
        unsubscribe && unsubscribe();
        commit('removeAccounts')
    },
    async setBalanceAction({commit}: ActionContext<PortalState, PortalState>, balance: number ){
        commit('setBalance', {balance})
    },
    async setCurrentAccountIDAction({commit}: ActionContext<PortalState, PortalState>, address: string ){
        commit('setCurrentAccountID', {address})
    },
    async setAPIAction({commit}: ActionContext<PortalState, PortalState>, api: any ){
        commit('setBalance', {api})
    },
  
}

